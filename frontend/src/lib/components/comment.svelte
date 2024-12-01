<script>
  import * as Card from "$lib/components/ui/card";
  import { activeUser } from "../../userStore";
  import { Button } from "$lib/components/ui/button";

  export let commentId;
  export let comment;
  export let commentator;
  export let postedDateComment;
  export let selected; // Current "selected" status of the comment
  export let threadOwner; // Owner of the thread

  let currentUser = null;

  // Function to toggle the helpful status
  const toggleHelpful = async () => {
    try {
      const response = await fetch(`https://threef.vercel.app/api/comments/${commentId}/toggle-selected/`, {
        method: "PATCH",
        headers: {
          "Content-Type": "application/json",
        },
      });

      if (!response.ok) {
        console.error("Failed to toggle helpful status");
        return;
      }

      const data = await response.json();
      selected = data.selected; // Update the local "selected" state
    } catch (error) {
      console.error("Error toggling helpful status:", error);
    }
  };

  // Subscribe to the active user
  $: activeUser.subscribe((value) => {
    currentUser = value;
  });

  // Format the date to a human-readable format
  const formatDate = (isoDate) => {
    if (!isoDate) return "";
    const date = new Date(isoDate);
    return new Intl.DateTimeFormat("en-US", {
      year: "numeric",
      month: "long",
      day: "numeric",
      hour: "numeric",
      minute: "numeric",
      hour12: true,
    }).format(date);
  };
</script>

<div class="flex w-full pb-2">
  <Card.Root class={`w-full bg-opacity-90 hover:bg-opacity-100 relative ${selected ? 'border-2 border-teal-600 dark:border-teal-800' : ''}`}>
    <div class="flex items-center w-full">
      <div class="flex flex-col pb-2 w-full">
        <Card.Header>
          <Card.Title class="w-full flex items-center">
            {comment}
            {#if selected}
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" class="ml-2 size-5 text-teal-800">
                <path stroke-linecap="round" stroke-linejoin="round" d="M6.633 10.25c.806 0 1.533-.446 2.031-1.08a9.041 9.041 0 0 1 2.861-2.4c.723-.384 1.35-.956 1.653-1.715a4.498 4.498 0 0 0 .322-1.672V2.75a.75.75 0 0 1 .75-.75 2.25 2.25 0 0 1 2.25 2.25c0 1.152-.26 2.243-.723 3.218-.266.558.107 1.282.725 1.282m0 0h3.126c1.026 0 1.945.694 2.054 1.715.045.422.068.85.068 1.285a11.95 11.95 0 0 1-2.649 7.521c-.388.482-.987.729-1.605.729H13.48c-.483 0-.964-.078-1.423-.23l-3.114-1.04a4.501 4.501 0 0 0-1.423-.23H5.904m10.598-9.75H14.25M5.904 18.5c.083.205.173.405.27.602.197.4-.078.898-.523.898h-.908c-.889 0-1.713-.518-1.972-1.368a12 12 0 0 1-.521-3.507c0-1.553.295-3.036.831-4.398C3.387 9.953 4.167 9.5 5 9.5h1.053c.472 0 .745.556.5.96a8.958 8.958 0 0 0-1.302 4.665c0 1.194.232 2.333.654 3.375Z" />
              </svg>
            {/if}
          </Card.Title>
        </Card.Header>

        <Card.Description class="flex flex-col w-full p-3 pl-6">
          <span>
            <a href={`/user/${commentator}`} class="hover:text-rose-900 hover:underline font-bold">
              {commentator}
            </a>
            at {formatDate(postedDateComment)}
          </span>

          {#if currentUser === threadOwner}
            <Button 
              on:click={toggleHelpful} 
              class="w-full mt-4 hover:bg-rose-900">
              {selected ? "Unmark as Helpful" : "Mark as Helpful"}
            </Button>
          {/if}
        </Card.Description>
      </div>
    </div>
  </Card.Root>
</div>

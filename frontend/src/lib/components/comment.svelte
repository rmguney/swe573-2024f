<script>
  import * as Card from "$lib/components/ui/card";
  export let commentId;
  export let comment;
  export let commentator;
  export let postedDateComment;

/*   export let voteCountComment;
  
const endPoint = 'https://threef.vercel.app/api/voteCountComment/';

  // Function to handle voting
  async function handleVote(voteType) {
    try {
      const response = await fetch(endPoint, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ id: commentId, vote_type: voteType }), // Sending `id` and `vote_type`
      });

      if (response.ok) {
        const data = await response.json();
        // Update the vote count locally
        voteCountComment = data.voteCountComment;
      } else {
        const errorText = await response.json();
        console.error("Failed to vote:", errorText);
      }
    } catch (error) {
      console.error("Error during voting:", error);
    }
  } */
</script>

<div class="flex w-full pb-2">
  <Card.Root class="w-full bg-opacity-90 hover:bg-opacity-100">
    <div class="flex items-center w-full">
<!--       <div class="flex flex-col items-center justify-center w-12 h-24 translate-x-4">
        <button 
          class="block w-10 h-6 hover:text-rose-900"
          on:click={() => handleVote('upvote')}
        >
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-full h-full">
            <path stroke-linecap="round" stroke-linejoin="round" d="m4.5 15.75 7.5-7.5 7.5 7.5" />
          </svg>
        </button>

        <div class="py-1">
          {voteCountComment}
        </div>

        <button 
          class="block w-6 h-6 hover:text-rose-900"
          on:click={() => handleVote('downvote')}
        >
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-full h-full">
            <path stroke-linecap="round" stroke-linejoin="round" d="m19.5 8.25-7.5 7.5-7.5-7.5" />
          </svg>
        </button>
      </div> -->

      <div class="flex flex-col pb-2 w-full">
        <Card.Header>
          <Card.Title class="w-full">
            {comment}
          </Card.Title>
        </Card.Header>

        <Card.Description class="w-full p-3 pl-6">
          <small>
            at {postedDateComment} by <a href="/" class="text-rose-900 hover:underline font-bold">{commentator}</a>
          </small>
          <small class="hidden">
            {commentId}
          </small>
        </Card.Description>
      </div>
    </div>
  </Card.Root>
</div>

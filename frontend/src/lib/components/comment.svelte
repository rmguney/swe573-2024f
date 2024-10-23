<script>
  import * as Card from "$lib/components/ui/card";
  export let commentId;
  export let comment;
  export let voteCountComment;
  export let commentator;
  export let postedDateComment;
</script>

<div class="flex w-full pb-2">
  <Card.Root class="w-full bg-opacity-90 hover:bg-opacity-100">
    <div class="flex items-center w-full">
      <div class="flex flex-col items-center justify-center w-12 h-24 translate-x-4">
        <button class="block w-10 h-6 hover:text-rose-900">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-full h-full">
            <path stroke-linecap="round" stroke-linejoin="round" d="m4.5 15.75 7.5-7.5 7.5 7.5" />
          </svg>
        </button>

        <div class="py-1">
          {voteCountComment}
        </div>

        <button class="block w-6 h-6 hover:text-rose-900">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-full h-full">
            <path stroke-linecap="round" stroke-linejoin="round" d="m19.5 8.25-7.5 7.5-7.5-7.5" />
          </svg>
        </button>
      </div>

      <div class="flex flex-col pl-4 w-full">
        <Card.Header>
          <Card.Title class="w-full">
            {comment}
          </Card.Title>
        </Card.Header>

        <Card.Description class="w-full p-3 pl-6">
          <small>
            {voteCountComment} by {commentator} {postedDateComment} ago
          </small>
          <small class="hidden">
            {commentId}
          </small>
        </Card.Description>
      </div>
    </div>
  </Card.Root>
</div>

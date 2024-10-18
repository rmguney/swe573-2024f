<script>
  import { Textarea } from "$lib/components/ui/textarea";
  import { Button } from "$lib/components/ui/button";
  import * as Card from "$lib/components/ui/card";
  import Post from '$lib/components/post.svelte';
  import Comment from '$lib/components/comment.svelte';
  import { threadStore } from '../../../threadStore';

  export let data;

  let thread = $threadStore.find(thread => thread.id == data.id);
</script>

<div class="flex flex-col items-center bg-gradient-to-br from-[#c08081] to-[#49796b] p-8">
  <div class="w-full lg:w-2/3">
    <Post
      id={data.id}
      title={thread.title}
      description={thread.description}
      imageSrc={thread.imageSrc}
      postedBy={thread.postedBy}
      timeAgo={thread.timeAgo}
      voteCount={thread.voteCount}
      variant="thread"
    />
    <Card.Root class="bg-opacity-90 hover:bg-opacity-100 p-4 mt-4 flex flex-col">
      <Textarea class="h-20 resize-none p-2" placeholder="Say stuff" />
      <Button class="w-full mt-2">Send</Button>
    </Card.Root>

    <div class="flex flex-col justify-center pt-6">
      {#if thread.comments && thread.comments.length > 0}
        {#each thread.comments as comment}
          <Comment
            comment={comment.comment}
            voteCountComment={comment.voteCountComment}
            commentator={comment.commentator}
            timeAgoComment={comment.timeAgoComment}
          />
        {/each}
      {:else}
        <Card.Root class="bg-opacity-90 hover:bg-opacity-100 mt-4">
          <Card.Header>
            <Card.Title class="pb-2 text-lg text-center">There are no comments yet</Card.Title>
          </Card.Header>
          <Card.Description class="p-4 text-center">
            Be the first to comment on this thread!
          </Card.Description>
        </Card.Root>
      {/if}
    </div>
  </div>
</div>

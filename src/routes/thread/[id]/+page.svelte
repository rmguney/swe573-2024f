<script>
    import { Textarea } from "$lib/components/ui/textarea";
    import { Button } from "$lib/components/ui/button";
    import * as Card from "$lib/components/ui/card";
    import Post from '$lib/components/post.svelte';
    import Comment from '$lib/components/comment.svelte';
    import Suggestions from '$lib/components/suggestions.svelte';
    import { threadStore } from '../../../threadStore';
  
    export let data;
  
    let thread = $threadStore.find(thread => thread.id == data.id);
  </script>
  
  <div class="flex flex-row bg-gradient-to-br from-[#c08081] to-[#49796b]">
    <div class="p-8 flex flex-col w-full">
      <div class="w-full">
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
      <Card.Root class="bg-opacity-90 hover:bg-opacity-100 w-auto p-4 mt-2 flex flex-col">
        <Textarea class="h-20 resize-none p-2" placeholder="Say stuff" />
        <Button class="w-full mt-2">Send</Button>
      </Card.Root>
    </div>
      <div class="flex flex-col lg:flex-row justify-center">
        <div class="lg:w-1/3 pt-8 lg:pr-8">
          <Suggestions class="p-4" />
        </div>
        <div class="flex flex-wrap justify-center pt-6 lg:w-2/3">
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
            <div class="-translate-x-8 w-full p-4 pt-2">
              <Card.Root class="bg-opacity-90 hover:bg-opacity-100">
                <Card.Header>
                  <Card.Title class="pb-2 text-lg hidden lg:block">There are no comments yet</Card.Title>
                </Card.Header>
                <Card.Description class="p-4 pl-6 text-md pb-6">
                  Be the first to comment on this thread!
                </Card.Description>
              </Card.Root>
            </div>
          {/if}
        </div>
    </div>
    </div>
  </div>
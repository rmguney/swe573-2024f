<script>
    import { ScrollArea } from "$lib/components/ui/scroll-area/index.js";
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
  
  <div class="flex flex-row fixed">
    <div class="w-[50rem] p-8 flex flex-col">
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

    <div class="w-auto pt-8 pr-8 [50rem]">
      <Suggestions class="p-4" />
    </div>
    <div class="flex flex-col justify-center w-2/3">

      <ScrollArea class="w-full h-[49rem]">
        <div class="flex flex-wrap justify-center pt-2 pr-8">
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
            <div class="pt-6 -translate-x-8">
              <Card.Root class="bg-opacity-90 hover:bg-opacity-100 w-[50rem]">
                <Card.Header>
                  <Card.Title class="pb-2 text-lg">There are no comments yet</Card.Title>
                </Card.Header>
                <Card.Description class="p-4 pl-6 text-md pb-6">
                  Be the first to comment on this thread!
                </Card.Description>
              </Card.Root>
            </div>
          {/if}
        </div>
      </ScrollArea>
    </div>
  </div>
  
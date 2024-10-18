<script>
  import { Textarea } from "$lib/components/ui/textarea";
  import { Button } from "$lib/components/ui/button";
  import * as Card from "$lib/components/ui/card";
  import Post from '$lib/components/post.svelte';
  import Comment from '$lib/components/comment.svelte';
  import { threadStore } from '../../../threadStore';

  export let data;
  let comment = '';

  let handleDownvote = () => {
  threadStore.update((prev) => {
    return prev.map((thread) => {
      if (thread.id == id) {
        return {
          ...thread,
          voteCount: thread.voteCount - 1
        };
      }
      return thread;
    });
  });
};

let handleUpvote = () => {
  threadStore.update((prev) => {
    return prev.map((thread) => {
      if (thread.id == id) {
        return {
          ...thread,
          voteCount: thread.voteCount + 1
        };
      }
      return thread;
    });
  });
};

let handleUpvoteComment = () => {
  threadStore.update((prev) => {
    return prev.map((thread) => {
      if (thread.id == id) {
        return {
          ...thread,
          voteCountComment: comment.voteCountComment + 1
        };
      }
      return thread;
    });
  });
};

let handleDownvoteComment = () => {
  threadStore.update((prev) => {
    return prev.map((thread) => {
      if (thread.id == id) {
        return {
          ...thread,
          voteCountComment: comment.voteCountComment - 1
        };
      }
      return thread;
    });
  });
};

  let handleSend = () => {
    threadStore.update(prev => {

      const lastCommentId = prev.find(thread => thread.id == data.id)?.comments?.slice(-1)[0]?.commentId || 0;

      let newComment = {
        commentId: lastCommentId + 1,
        comment,
        voteCountComment: 0,
        commentator: 'Anonymous',
        timeAgoComment: '0 hours'
      };

      return prev.map(thread => {
        if (thread.id == data.id) {
          return {
            ...thread,
            comments: [...thread.comments, newComment]
          };
        }
        return thread;
      });
    });
  };

  $: thread = $threadStore.find(thread => thread.id == data.id);
</script>

<div class="flex flex-col items-center bg-gradient-to-br from-[#c08081] to-[#49796b] p-8">
  <div class="w-full lg:w-2/3">
    <Post bind:handleDownvote={handleDownvote}
    bind:handleUpvote={handleUpvote}
      id={data.id}
      title={thread.title}
      description={thread.description}
      tags={thread.tags}
      imageSrc={thread.imageSrc}
      postedBy={thread.postedBy}
      timeAgo={thread.timeAgo}
      voteCount={thread.voteCount}
      variant="thread"
    />
    <Card.Root class="bg-opacity-90 hover:bg-opacity-100 p-4 mt-4 flex flex-col">
      <Textarea bind:value={comment} class="h-20 resize-none p-2" placeholder="Say stuff" />

      <Button on:click={handleSend} class="w-full mt-2 hover:bg-rose-900">Send</Button>
    </Card.Root>

    <div class="flex flex-col justify-center pt-4">
      {#if thread.comments && thread.comments.length > 0}
        {#each thread.comments as comment}
          <Comment bind:handleDownvoteComment={handleDownvoteComment}
          bind:handleUpvoteComment={handleUpvoteComment}
            commentId={comment.commentId}
            comment={comment.comment}
            voteCountComment={comment.voteCountComment}
            commentator={comment.commentator}
            timeAgoComment={comment.timeAgoComment}
          />
        {/each}
      {:else}
        <Card.Root class="bg-opacity-90 hover:bg-opacity-100">
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

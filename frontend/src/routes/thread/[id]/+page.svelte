<script>
  import { Textarea } from "$lib/components/ui/textarea";
  import { Button } from "$lib/components/ui/button";
  import * as Card from "$lib/components/ui/card";
  import Post from '$lib/components/post.svelte';
  import Comment from '$lib/components/comment.svelte';
  import { threadStore } from '../../../threadStore';
  import { commentStore } from '../../../commentStore'; 
  import { onMount } from 'svelte';

  export let data;

  let thread = null;
  let threadComments = [];
  let newCommentText = '';

  // Fetch the thread and its corresponding comments
  onMount(() => {
    thread = $threadStore.find(t => t.id == data.id);

    // Fetch the comments for the current thread
    commentStore.subscribe(comments => {
      threadComments = comments.filter(comment => comment.threadId === data.id);
    });
  });

  let handleComment = () => {
    if (!newCommentText.trim()) {
      alert('Comment cannot be empty!');
      return;
    }

    commentStore.update(prev => {
      let newCommentId = prev.filter(comment => comment.threadId === data.id).length + 1;

      let newComment = {
        threadId: data.id, // Link comment to the correct thread
        commentId: newCommentId,
        comment: newCommentText,
        voteCountComment: 0,
        commentator: "You", // You can change this to dynamic user
        timeAgoComment: "Just now"
      };

      return [...prev, newComment];
    });

    newCommentText = ''; // Clear input after submission
  };
</script>

<div class="flex flex-col items-center bg-gradient-to-br from-[#c08081] to-[#49796b] p-8">
  <div class="w-full lg:w-2/3">
    {#if thread}
      <Post
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
        <Textarea
          bind:value={newCommentText}
          class="h-20 resize-none p-2"
          placeholder="Say something"
        />
        <Button on:click={handleComment} class="w-full mt-2 hover:bg-rose-900">
          Send
        </Button>
      </Card.Root>

      <div class="flex flex-col justify-center pt-4">
        {#if threadComments.length > 0}
          {#each threadComments as comment}
            <Comment
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
    {:else}
      <p>Loading...</p>
    {/if}
  </div>
</div>

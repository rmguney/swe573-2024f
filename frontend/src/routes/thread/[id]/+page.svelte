<script>
  import { Textarea } from "$lib/components/ui/textarea";
  import { Button } from "$lib/components/ui/button";
  import * as Card from "$lib/components/ui/card";
  import Post from '$lib/components/post.svelte';
  import Comment from '$lib/components/comment.svelte';
  import { threadStore } from '../../../threadStore';

  export let data;
  let comment = '';

  let handleSend = async () => {
    if (!comment.trim()) {
        console.error("Comment cannot be empty");
        return;
    }

    const endPoint = `http://localhost:8000/api/comment/`;
    const payload = {
        thread: data.id,
        comment: comment,
        voteCountComment: 0,
        commentator: 'Anonymous',
        postedDateComment: new Date().toISOString(),
    };

    try {
        const response = await fetch(endPoint, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(payload),
        });

        if (!response.ok) {
            const errData = await response.json();
            throw new Error(JSON.stringify(errData));
        }

        const newComment = await response.json();

        threadStore.update(prev => {
            return prev.map(thread => {
                if (thread.id == data.id) {
                    const comments = thread.comments ? thread.comments : [];
                    return {
                        ...thread,
                        comments: [...comments, newComment]
                    };
                }
                return thread;
            });
        });

        comment = ''; 
    } catch (error) {
        console.error('Error submitting comment:', error);
    }
  };

  $: thread = $threadStore.find(thread => thread.id == data.id);
</script>

<div class="flex flex-col items-center bg-gradient-to-br from-[#c08081] to-[#49796b] p-8">
  <div class="w-full lg:w-2/3">
    <Post 
      id={data.id}
      title={thread.title}
      description={thread.description}
      tags={thread.tags}
      imageSrc={thread.imageSrc}
      postedBy={thread.postedBy}
      postedDate={thread.postedDate}
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
          <Comment
            commentId={comment.commentId}
            comment={comment.comment}
            voteCountComment={comment.voteCountComment}
            commentator={comment.commentator}
            postedDateComment={comment.postedDateComment}
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
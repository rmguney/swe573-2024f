<script>
  import Post from '$lib/components/post.svelte';
  import { threadStore } from '../../threadStore';
</script>

<div class="flex">
    <div class="flex flex-col gap-4 m-8 lg:flex-row lg:flex-wrap lg:justify-center">
      {#each $threadStore as thread}
        <a href={`/thread/${thread.id}`} 
           class=" w-1/3 w-[calc(33.333%-1rem)]">
          <Post
            id={thread.id}
            title={thread.title}
            description={thread.description}
            imageSrc={thread.imageSrc}
            postedBy={thread.postedBy}
            timeAgo={thread.timeAgo}
            voteCount={thread.voteCount}
            variant="thumb"
          />
        </a>
      {/each}
    </div>
</div>
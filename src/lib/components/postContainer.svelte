<script>
  import Post from '$lib/components/post.svelte';
  import { threadStore } from '../../threadStore';
</script>

{#each $threadStore as thread}
<a href={`/thread/${thread.id}`} class="w-[calc(33.333%-1rem)]">
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
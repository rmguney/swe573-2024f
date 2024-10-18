<script>
  import Post from '$lib/components/post.svelte';
  import { threadStore } from '../../threadStore';
</script>

{#each $threadStore.slice().sort((a, b) => b.id - a.id) as thread}
<a href={`/thread/${thread.id}`} class="w-full lg:w-[calc(33.333%-1rem)]">
  <Post
    id={thread.id}
    title={thread.title}
    description={thread.description}
    tags={thread.tags}
    imageSrc={thread.imageSrc}
    postedBy={thread.postedBy}
    timeAgo={thread.timeAgo}
    voteCount={thread.voteCount}
    variant="thumb"
  />
</a>
{/each}

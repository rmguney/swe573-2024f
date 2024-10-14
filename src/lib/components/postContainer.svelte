<script>
  import { ScrollArea } from "$lib/components/ui/scroll-area/index.js";
  import Button from './ui/button/button.svelte';

  import Post from '$lib/components/post.svelte';
  import {threadStore} from '../../threadStore';
</script>

<div class="flex justify-center">
  <ScrollArea class="h-[50rem] w-[90rem]">
    <div class="flex flex-wrap justify-center gap-4 m-8">
      {#each $threadStore as thread}
        <a href={`/thread/${thread.id}`} 
           class="w-[calc(33.333%-1rem)] min-w-[20rem]">
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
  </ScrollArea>
</div>
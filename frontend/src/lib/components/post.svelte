<script>
  import * as Card from "$lib/components/ui/card";

  export let id;
  export let title;
  export let imageSrc;
  export let postedBy;
  export let timeAgo;
  export let voteCount;  
  export let description;  
  export let variant = "thumb";
</script>

<Card.Root 
  class={`shadow-lg hover:shadow-xl transition duration-300
  ${variant === "thumb" ? 'grayscale hover:grayscale-0 bg-opacity-75 hover:bg-opacity-100 w-70 h-70 ' : 'bg-opacity-90 hover:bg-opacity-100'}`}>
  <Card.Header>
    <div class="flex flex-row items-center">
      {#if variant !== 'thumb'}
      <div class="flex flex-col items-center justify-center p-2 -translate-x-3">
        <a href="#upvote" class="block w-6 h-6 mb-2 hover:text-rose-900">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-full h-full">
            <path stroke-linecap="round" stroke-linejoin="round" d="m4.5 15.75 7.5-7.5 7.5 7.5" />
          </svg>
        </a>
        <div class="py-1">
          {voteCount}
        </div>
        <a href="#downvote" class="block w-6 h-6 mt-2 hover:text-rose-900">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-full h-full">
            <path stroke-linecap="round" stroke-linejoin="round" d="m19.5 8.25-7.5 7.5-7.5-7.5" />
          </svg>        
        </a>
      </div>
      {/if}

      <div class="flex-1 min-w-0">
        <Card.Title>
          <div class="hidden">{id}</div>
          <div class={`${variant === "thumb" ? 'text-ellipsis overflow-hidden whitespace-nowrap w-full max-w-full' : ''}`}>
            {title}
          </div>
        </Card.Title>
        <Card.Description class="pt-3">
          <small class={`${variant === "thumb" ? 'text-ellipsis overflow-hidden whitespace-nowrap w-full max-w-full' : 'hidden'}`}>
            {voteCount} points •
          </small>
          <small class={`${variant === "thumb" ? 'text-ellipsis overflow-hidden whitespace-nowrap w-full max-w-full' : ''}`}>
          {timeAgo} ago by {postedBy}
          </small>
        </Card.Description>
      </div>
    </div>
  </Card.Header>
  <Card.Content>
    <div class={`${variant === "thumb" ? 'hidden' : ''}`}>
      {description}
    </div>
    <div class={`${variant === "thumb" ? 'overflow-hidden flex justify-center items-center' : ''}`}>
      {#if variant !== 'thumb'}
        <a href={imageSrc} target="_blank" rel="noopener noreferrer">
          <img class="object-cover w-full h-80 pt-6" src={imageSrc} alt={title} />
        </a>
      {:else}
        <img class="object-cover w-full h-44" src={imageSrc} alt={title} />
      {/if}
    </div>
  </Card.Content>
</Card.Root>

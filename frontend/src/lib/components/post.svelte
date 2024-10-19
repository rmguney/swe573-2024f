<script>
  import * as Card from "$lib/components/ui/card";
  import { onMount } from 'svelte';
  import { writable } from 'svelte/store';

  export let id;
  export let title;
  export let tags;
  export let imageSrc;
  export let postedBy;
  export let timeAgo;
  export let voteCount;  
  export let description;
  export let variant = "thumb";
  export let handleDownvote;
  export let handleUpvote;

  let tagDetails = writable([]);

  const fetchTagDetails = async () => {
    let fetchedTags = await Promise.all(tags.map(async (qcode) => {
      try {
        const response = await fetch(`https://www.wikidata.org/w/api.php?action=wbgetentities&ids=${qcode}&format=json&languages=en&props=labels|descriptions&origin=*`);
        const data = await response.json();
        const entity = data.entities[qcode];
        return {
          label: entity.labels?.en?.value || 'Unknown label',
          description: entity.descriptions?.en?.value || 'No description',
          id: qcode
        };
      } catch (error) {
        console.error('Failed to fetch tag details:', error);
        return { label: 'Unknown label', description: 'No description', id: qcode };
      }
    }));
    tagDetails.set(fetchedTags);
  };

  onMount(fetchTagDetails);
</script>

<Card.Root 
  class={`shadow-lg hover:shadow-xl transition duration-300
  ${variant === "thumb" ? 'grayscale hover:grayscale-0 bg-opacity-75 hover:bg-opacity-100 w-70 h-70 hover:scale-110' : 'bg-opacity-90 hover:bg-opacity-100'}`}>
  <Card.Header>
    <div class="flex flex-row items-center">
      {#if variant !== 'thumb'}
      <div class="flex flex-col items-center justify-center p-2 -translate-x-3">
        <button on:click={handleUpvote} class="block w-6 h-6 mb-2 hover:text-rose-900">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-full h-full">
            <path stroke-linecap="round" stroke-linejoin="round" d="m4.5 15.75 7.5-7.5 7.5 7.5" />
          </svg>
        </button>
        <div class="py-1">
          {voteCount}
        </div>
        <button on:click={handleDownvote}  class="block w-6 h-6 mt-2 hover:text-rose-900">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-full h-full">
            <path stroke-linecap="round" stroke-linejoin="round" d="m19.5 8.25-7.5 7.5-7.5-7.5" />
          </svg>        
        </button>
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
          <div class={`${variant === "thumb" ? 'hidden' : 'pt-2'}`}>
            <ul>
              <h2 class="text-md font-semibold text-black dark:text-white">Tags:</h2>
              {#each $tagDetails as tag}
                <li class="mt-2">
                  <a 
                    href={`https://www.wikidata.org/wiki/${tag.id}`} 
                    target="_blank" 
                    rel="noopener noreferrer"
                    class="underline text-black dark:text-white hover:text-rose-700 dark:hover:text-rose-900"
                  >
                    {tag.label}: {tag.description}
                  </a>
                </li>
              {/each}
            </ul>
          </div>
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

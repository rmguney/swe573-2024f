<script>
  import * as Card from "$lib/components/ui/card";
  import { onMount } from "svelte";
  import { updateThreadVote } from "../../threadStore";
  import { writable } from "svelte/store";

  export let id = '';
  export let title = '';
  export let tags = [];
  export let imageSrc = '';
  export let postedBy = '';
  export let postedDate = '';
  export let voteCount = 0;
  export let description = '';
  export let material = '';
  export let size = '';
  export let shape = '';
  export let color = '';
  export let texture = '';
  export let weight = '';
  export let smell = '';
  export let marking = '';
  export let functionality = '';
  export let period = '';
  export let location = '';
  export let variant = "thumb";

  let tagDetails = writable([]);

  const fetchTagDetails = async () => {
    if (!tags.length) {
      console.log("No tags provided.");
      return;
    }
    try {
      let fetchedTags = await Promise.all(tags.map(async (qcode) => {
        const response = await fetch(`https://www.wikidata.org/w/api.php?action=wbgetentities&ids=${qcode}&format=json&languages=en&props=labels|descriptions&origin=*`);
        const data = await response.json();
        const entity = data.entities[qcode];
        return {
          label: entity.labels?.en?.value || 'Unknown label',
          description: entity.descriptions?.en?.value || 'No description',
          id: qcode
        };
      }));
      tagDetails.set(fetchedTags);
    } catch (error) {
      console.error("Failed to fetch tag details:", error);
    }
  };

  const threadVoteEndPoint = 'https://threef.vercel.app/api/voteCount/'; // Updated endpoint

  async function handleVote(voteType) {
    try {
      const response = await fetch(threadVoteEndPoint, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ id: id, vote_type: voteType }), // Pass only `id` and `vote_type`
      });

      if (!response.ok) {
        const errorText = await response.text();
        console.error("Error response from server:", errorText);
        return;
      }

      const data = await response.json();
      updateThreadVote(id, data.voteCount);
      voteCount = data.voteCount; // Update local state for immediate feedback
    } catch (error) {
      console.error("Error during voting:", error);
    }
  }

  onMount(fetchTagDetails);
</script>

<Card.Root 
  class={`shadow-lg hover:shadow-xl transition duration-300
  ${variant === "thumb" ? 'grayscale hover:grayscale-0 bg-opacity-75 hover:bg-opacity-100 w-70 h-70 lg:hover:scale-110' : 'bg-opacity-90 hover:bg-opacity-100'}`}>
  <Card.Header>
    <div class="flex flex-row items-center">
      {#if variant !== 'thumb'}
      <div class="flex flex-col items-center justify-center p-2 -translate-x-3">
        <button 
          class="block w-6 h-6 mb-2 hover:text-rose-900"
          on:click={() => handleVote('upvote')}
        >
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-full h-full">
            <path stroke-linecap="round" stroke-linejoin="round" d="m4.5 15.75 7.5-7.5 7.5 7.5" />
          </svg>
        </button>
        <div class="py-1">
          {voteCount}
        </div>
        <button 
          class="block w-6 h-6 mt-2 hover:text-rose-900"
          on:click={() => handleVote('downvote')}
        >
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
          <small class={`${variant === "thumb" ? 'overflow-hidden whitespace-wrap w-full max-w-full' : ''}`}>
            at {postedDate} by <a href="/" class="text-rose-900 hover:underline font-bold">{postedBy}</a>
          </small>
        </Card.Description>
      </div>
    </div>
  </Card.Header>
<Card.Content>
  <div class={`${variant !== "thumb" ? 'flex flex-col' : ''}`}>
    <div class={`${variant === "thumb" ? 'hidden' : 'p-4'}`}>
      <ul>
        {#if material}<li class="mt-2"><strong>Material:</strong> {material}</li>{/if}
        {#if size}<li class="mt-2"><strong>Size:</strong> {size}</li>{/if}
        {#if shape}<li class="mt-2"><strong>Shape:</strong> {shape}</li>{/if}
        {#if color}<li class="mt-2"><strong>Color:</strong> {color}</li>{/if}
        {#if texture}<li class="mt-2"><strong>Texture:</strong> {texture}</li>{/if}
        {#if weight}<li class="mt-2"><strong>Weight:</strong> {weight}</li>{/if}
        {#if smell}<li class="mt-2"><strong>Smell:</strong> {smell}</li>{/if}
        {#if marking}<li class="mt-2"><strong>Marking:</strong> {marking}</li>{/if}
        {#if functionality}<li class="mt-2"><strong>Functionality:</strong> {functionality}</li>{/if}
        {#if period}<li class="mt-2"><strong>Period:</strong> {period}</li>{/if}
        {#if location}<li class="mt-2"><strong>Location:</strong> {location}</li>{/if}
        {#if description}<li class="mt-2"><strong>Description:</strong> {description}</li>{/if}
      </ul>      
    </div>
    <div class={`${variant === "thumb" ? 'overflow-hidden flex justify-center items-center' : ''}`}>
      {#if variant !== 'thumb'}
        <a href={imageSrc} target="_blank" rel="noopener noreferrer">
          {#if imageSrc && (imageSrc.endsWith('.mp4') || imageSrc.endsWith('.webm') || imageSrc.endsWith('.ogg'))}
            <!-- svelte-ignore a11y-media-has-caption -->
            <video class="object-cover w-full pt-6" src={imageSrc} controls />
          {:else if imageSrc}
            <img class="object-cover w-full pt-6" src={imageSrc} alt={title} />
          {/if}
        </a>
      {:else if imageSrc}
        <!-- svelte-ignore a11y-media-has-caption -->
        {#if imageSrc.endsWith('.mp4') || imageSrc.endsWith('.webm') || imageSrc.endsWith('.ogg')}
          <video class="object-cover w-full h-44" src={imageSrc}/>
        {:else}
          <img class="object-cover w-full h-44" src={imageSrc} alt={title} />
        {/if}
      {/if}
    </div>
  </div>
</Card.Content>
</Card.Root>

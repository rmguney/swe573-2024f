<script>
  import * as Card from "$lib/components/ui/card";
  import { onMount } from "svelte";
//  import { updateThreadVote } from "../../threadStore";
  import { writable } from "svelte/store";
  import { activeUser } from "../../userStore";
  import { Button } from "$lib/components/ui/button";

  export let id = '';
  export let title = '';
  export let tags = [];
  export let imageSrc = '';
  export let postedBy = '';
  export let postedDate = '';
 // export let voteCount = 0;
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
  export let resolved = false;
  export let variant = "thumb";

  let tagDetails = writable([]);
  let currentUser = null; 

  const fetchThreadDetails = async () => {
    try {
        const response = await fetch(`https://threef.vercel.app/api/threads/${id}`);
        if (!response.ok) {
            throw new Error("Failed to fetch thread details");
        }
        const threadData = await response.json();

        resolved = threadData.resolved;
    } catch (error) {
        console.error("Error fetching thread details:", error);
    }
};


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

  const threadVoteEndPoint = 'https://threef.vercel.app/api/voteCount/';

/*   async function handleVote(voteType) {
    try {
      const response = await fetch(threadVoteEndPoint, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ id: id, vote_type: voteType }), 
      });

      if (!response.ok) {
        const errorText = await response.text();
        console.error("Error response from server:", errorText);
        return;
      }

      const data = await response.json();
      updateThreadVote(id, data.voteCount);
      voteCount = data.voteCount; 
    } catch (error) {
      console.error("Error during voting:", error);
    }
  } */

  const toggleResolved = async () => {
    if (currentUser !== postedBy) return;
    try {
        const response = await fetch(`https://threef.vercel.app/api/threads/${id}/updateResolved`, {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ resolved: !resolved }),
        });

        if (!response.ok) {
            console.error("Failed to toggle resolved status");
            return;
        }

        const data = await response.json();
        resolved = data.resolved; 
    } catch (error) {
        console.error("Error toggling resolved status:", error);
    }
};

  $: activeUser.subscribe((value) => {
    currentUser = value;
  });

  onMount(() => {
    fetchThreadDetails(); 
    fetchTagDetails(); 
  });
</script>

<Card.Root 
  class={`shadow-lg hover:shadow-xl transition duration-300
  ${variant === "thumb" ? 'grayscale hover:grayscale-0 bg-opacity-75 hover:bg-opacity-100 w-70 h-70 lg:hover:scale-110' : 'bg-opacity-90 hover:bg-opacity-100'}`}>
  <Card.Header>
    <div class="flex flex-row items-center">
      <div class="flex-1 min-w-0">
        <Card.Title>
          <div class="hidden">{id}</div>
          <div class={`${variant === "thumb" ? 'text-ellipsis overflow-hidden whitespace-nowrap w-full max-w-full' : ''}`}>
            {title}
          </div>
        </Card.Title>
        <Card.Description class="pt-3">
          {#if resolved}
          <div class="flex items-center text-teal-600 font-semibold">
            <small class="text-teal-600 font-bold">Resolved</small>
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" class="w-4 h-4">
              <path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7" />
            </svg>
          </div>
          {:else}
          <div class="flex items-center text-rose-900 font-semibold">
            <small class="text-rose-900 font-bold">Unresolved</small>
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" class="w-4 h-4">
              <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </div>
          {/if}
          <small class={`${variant === "thumb" ? 'overflow-hidden whitespace-nowrap w-full max-w-full' : ''}`}>
            <a href="/" class="hover:text-rose-900 hover:underline font-bold">{postedBy}</a> at {postedDate}
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
                    class="hover:underline text-black dark:text-white hover:text-rose-700 dark:hover:text-rose-900"
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
  <div class={`${variant !== "thumb" ? 'flex flex-col' : ''}`}>
    <div class={`${variant === "thumb" ? 'hidden' : 'pt-0 pb-2'}`}>
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
    </div>
    <div class={`${variant === "thumb" ? 'overflow-hidden flex justify-center items-center' : ''}`}>
      {#if currentUser === postedBy}
      <Button 
        on:click={toggleResolved} 
        class={`${variant === "thumb" ? 'hidden' : 'w-full mt-2 hover:bg-rose-900'}`}>
        {resolved ? "Mark as Unresolved" : "Mark as Resolved"}
      </Button>
    {/if}
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
</Card.Content>
</Card.Root>

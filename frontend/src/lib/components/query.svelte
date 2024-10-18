<script>
  import { onMount } from 'svelte';
  import { writable } from 'svelte/store';

  let searchTerm = '';
  let searchResults = writable([]);
  let selectedItems = writable([]);
  let isLoading = writable(false);
  let showResults = writable(false);

  const searchWikidata = async () => {
    if (!searchTerm) {
      searchResults.set([]);
      showResults.set(false);
      return;
    }

    isLoading.set(true);
    showResults.set(true);

    try {
      const response = await fetch(`https://www.wikidata.org/w/api.php?action=wbsearchentities&search=${encodeURIComponent(searchTerm)}&language=en&format=json&origin=*`);
      const data = await response.json();
      searchResults.set(data.search);
    } catch (error) {
      console.error('Search failed', error);
      searchResults.set([]);
    } finally {
      isLoading.set(false);
    }
  };

  const selectItem = (item) => {
    selectedItems.update((items) => {
      if (!items.find((i) => i.id === item.id)) {
        return [...items, item];
      }
      return items;
    });
    showResults.set(false);
  };

  const removeSelectedItem = (itemId) => {
    selectedItems.update((items) => items.filter((i) => i.id !== itemId));
  };

  onMount(() => {
    const handleClickOutside = (event) => {
      const searchContainer = document.querySelector('.search-container');
      if (!searchContainer.contains(event.target)) {
        showResults.set(false);
      }
    };
    document.addEventListener('click', handleClickOutside);
    return () => document.removeEventListener('click', handleClickOutside);
  });

  $: tags = $selectedItems;
  export let tags;

</script>

<div class="w-full mx-auto relative search-container">
  <input
    type="text"
    placeholder="And add some relevant tags"
    bind:value={searchTerm}
    on:input={searchWikidata}
    class="w-full p-3 border border-black dark:border-white rounded-md text-black dark:text-white bg-white dark:bg-black text-sm"
  />

  {#if $isLoading}
    <p class="mt-2 text-black dark:text-white">Loading...</p>
  {/if}

  {#if $showResults && $searchResults.length > 0}
    <ul class="list-none p-0 mt-2 border border-black dark:border-white bg-white dark:bg-black rounded-md absolute w-full max-h-60 overflow-y-auto shadow-lg z-10">
      {#each $searchResults as result}
        <li class="mt-2">
          <button 
            on:click={() => selectItem(result)} 
            class="w-full text-left p-3 hover:bg-rose-900 hover:text-white text-black dark:text-white"
          >
            {result.label}: {result.description}
          </button>
        </li>
      {/each}
    </ul>
  {/if}

  <div class="selected-items mt-4">
    <h3 class="text-lg font-semibold text-black dark:text-white">Tags:</h3>
    <ul class="list-none p-0 mt-2">
      {#each $selectedItems as selectedItem}
        <li class="mt-2 flex items-center">
          <a 
            href={`https://www.wikidata.org/wiki/${selectedItem.id}`} 
            target="_blank" 
            rel="noopener noreferrer"
            class="underline text-black dark:text-white hover:text-rose-700 dark:hover:text-rose-900"
          >
            {selectedItem.label}: {selectedItem.description}
          </a>
          <button 
            on:click={() => removeSelectedItem(selectedItem.id)} 
            class="ml-4 bg-black dark:bg-white text-white dark:text-black py-1 px-3 rounded-md hover:bg-rose-900 hover:text-white"
          >
            Remove
          </button>
        </li>
      {/each}
    </ul>
  </div>
</div>

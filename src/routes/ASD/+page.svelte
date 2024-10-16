<script>
    let searchQuery = '';
    let results = [];
    let isLoading = false;
    let noResultsMessage = '';
    
    async function searchWikidata() {
      if (!searchQuery) return; 
    
      isLoading = true;
      noResultsMessage = '';
    
      const sparqlEndpoint = 'https://query.wikidata.org/sparql';
    
      const query = `
      SELECT ?item ?itemLabel ?itemDescription ?materialLabel WHERE {
        ?item rdfs:label ?itemLabel.
        FILTER(LANG(?itemLabel) = "en")
  
        OPTIONAL {
          ?item schema:description ?itemDescription.
          FILTER(LANG(?itemDescription) = "en")
        }
  
        OPTIONAL {
          ?item wdt:P186 ?material.
          ?material rdfs:label ?materialLabel.
          FILTER(LANG(?materialLabel) = "en")
        }
  
        FILTER(CONTAINS(LCASE(?itemLabel), "${searchQuery.toLowerCase()}") || 
               CONTAINS(LCASE(?itemDescription), "${searchQuery.toLowerCase()}") ||
               CONTAINS(LCASE(?materialLabel), "${searchQuery.toLowerCase()}"))
      }
      LIMIT 10`;
  
      const queryUrl = `${sparqlEndpoint}?query=${encodeURIComponent(query)}&format=json`;
    
      console.log('Generated SPARQL query URL:', queryUrl);
    
      try {
        const response = await fetch(queryUrl, {
          headers: {
            'Accept': 'application/sparql-results+json'
          }
        });
    
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
    
        const data = await response.json();
        const bindings = data.results.bindings;
    
        if (bindings.length === 0) {
          noResultsMessage = "No items found matching the search term.";
          results = [];
        } else {
          results = bindings.map(binding => ({
            label: binding.itemLabel?.value || 'No label available',
            description: binding.itemDescription?.value || 'No description available',
            material: binding.materialLabel?.value || 'No material available',
            link: binding.item.value
          }));
          noResultsMessage = "";
        }
      } catch (error) {
        console.error('Error fetching Wikidata:', error);
        noResultsMessage = "Error fetching data.";
        results = [];
      } finally {
        isLoading = false;
      }
    }
  </script>
  
  <div>
    <h3>Search Wikidata by Label, Description, or Material</h3>
    <input type="text" bind:value={searchQuery} placeholder="Search within labels, descriptions, or materials..." />
    <button on:click={searchWikidata}>Search</button>
  
    {#if isLoading}
      <p>Loading results...</p>
    {/if}
  
    {#if results.length > 0}
      <ul>
        {#each results as result}
          <li>
            <a href={result.link} target="_blank">
              <strong>{result.label}</strong>: {result.description}<br>
            </a>
          </li>
        {/each}
      </ul>
    {:else if !isLoading && noResultsMessage}
      <p>{noResultsMessage}</p>
    {/if}
  </div>
  
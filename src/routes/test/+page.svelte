<script>
    import { onMount } from 'svelte';

    let results = [];
    let noResultsMessage = ""; // To store a message if no results are found

    // List of available materials (Metallic Material, Textile, Plant Material, Glass, Plastic, Aggregate, Stone, Gemstone, Animal Product)
    let availableMaterials = [
        { label: 'Metallic', value: 'Q1924900' }, // Metallic Material (General)
        { label: 'Plant Matter', value: 'Q28969364' }, // Plant Material (General)
        { label: 'Animal Product', value: 'Q629103' }, // Animal Product (General)
        { label: 'Textile', value: 'Q28877' }, // Textile (General)
        { label: 'Glass', value: 'Q11469' }, // Glass (General)
        { label: 'Plastic', value: 'Q11472' }, // Plastic (General)
        { label: 'Aggregate', value: 'Q866298' }, // Aggregate (General)
        { label: 'Stone', value: 'Q22731' }, // Stone (General)
        { label: 'Gemstone', value: 'Q83437' }, // Gemstone (General)
    ];

    let selectedMaterial = 'Q1924900'; // Default selection is Metallic Material

    // Function to fetch data from Wikidata based on selected material
    async function fetchWikidata() {
        const sparqlQuery = buildSparqlQuery(selectedMaterial);
        console.log("Generated SPARQL query:", sparqlQuery); // Log the query for debugging
        const queryUrl = `https://query.wikidata.org/sparql?query=${encodeURIComponent(sparqlQuery)}&format=json`;

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

            // Check if results were found
            if (bindings.length === 0) {
                noResultsMessage = "No items found for the selected material.";
            } else {
                noResultsMessage = ""; // Clear the message if we have results
                results = bindings.map(binding => ({
                    label: binding.itemLabel ? binding.itemLabel.value : 'No label available',
                    description: binding.itemDescription ? binding.itemDescription.value : 'No description available',
                    materialLabel: binding.materialLabel ? binding.materialLabel.value : 'No material label available'
                }));
            }
        } catch (error) {
            console.error('Error fetching Wikidata:', error);
            noResultsMessage = "Error fetching data.";
        }
    }

    // Function to build the SPARQL query based on selected material
    function buildSparqlQuery(material) {
        return `
        SELECT DISTINCT ?item ?itemLabel ?itemDescription ?materialLabel WHERE {
        {
            # First condition: Items with material as the selected material or its subclasses
            OPTIONAL {
            ?item wdt:P186 ?material.
            ?material wdt:P279* wd:${material}.  # Material is a subclass of the selected material
            }
        }
        UNION
        {
            # Second condition: Items made from the selected material
            OPTIONAL {
            ?item wdt:P186 ?madeFromMaterial.
            ?madeFromMaterial wdt:P279* wd:${material}.  # Material is a subclass of the selected material
            }
        }

        # Ensure labels and descriptions are fetched
        SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
        }
        ORDER BY ?itemLabel
        LIMIT 20

        `;
    }

    // Fetch data from Wikidata when the page is loaded
    onMount(fetchWikidata);

    // Re-fetch data when the material is changed by the user
    function handleMaterialChange(event) {
        selectedMaterial = event.target.value;
        fetchWikidata(); // Re-fetch with the selected material
    }
</script>

<div>
    <h2>Choose a Material</h2>
    
    <!-- Dropdown to select material -->
    <select on:change={handleMaterialChange}>
        {#each availableMaterials as material}
            <option value={material.value} selected={selectedMaterial === material.value}>{material.label}</option>
        {/each}
    </select>

    {#if noResultsMessage}
        <p>{noResultsMessage}</p>
    {/if}

    <h2>Wikidata Query Results</h2>
    <ul>
        {#each results as result}
            <li>
                <strong>{result.materialLabel}</strong> - {result.description}
            </li>
        {/each}
    </ul>
</div>

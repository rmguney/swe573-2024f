<script>
    import * as Card from "$lib/components/ui/card/index.js";
    import { Button } from "$lib/components/ui/button";
    import Query from '$lib/components/query.svelte';
    import { threadStore } from "../../threadStore";
    import { goto } from '$app/navigation';
    import { activeUser } from '../../userStore';
    import { Input } from "$lib/components/ui/input/index.js";

    let title = '';
    let tags = [];
    let imageSrc; 
    let postedBy;
    let description = '';
    let material = '';
    let size = '';
    let shape = '';
    let color = '';
    let texture = '';
    let weight = '';
    let smell = '';
    let marking = '';
    let functionality = '';
    let period = '';
    let location = '';
    let anonymous = false; 
    let resolved = false;

    let errors = {
        title: '',
        image: ''
    };

    $: postedBy = $activeUser;

    function generateRandomString(length) {
        const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
        let result = '';
        for (let i = 0; i < length; i++) {
            result += characters.charAt(Math.floor(Math.random() * characters.length));
        }
        return result;
    }

    const uploadToSupabase = async (file) => {
        const supabaseUrl = import.meta.env.VITE_SUPABASE_URL;
        const anonKey = import.meta.env.VITE_SUPABASE_ANON_KEY;
        const bucketName = "threef_bucket";
        const fileExtension = file.name.split('.').pop();
        const fileName = `${generateRandomString(5)}.${fileExtension}`;

        const formData = new FormData();
        formData.append("file", file);

        const response = await fetch(`${supabaseUrl}/storage/v1/object/${bucketName}/${fileName}`, {
            method: "POST",
            headers: {
                "apikey": anonKey,
                "Authorization": `Bearer ${anonKey}`
            },
            body: formData
        });

        if (!response.ok) {
            const errorDetails = await response.json();
            console.error("Supabase upload error details:", errorDetails);
            throw new Error("Failed to upload image to Supabase");
        }

        return `${supabaseUrl}/storage/v1/object/public/${bucketName}/${fileName}`;
    };

    let handlePost = async () => {
        // Reset errors
        errors.title = '';
        errors.image = '';

        // Validation
        if (!title.trim()) {
            errors.title = 'Title is required.';
        }
        if (!imageSrc) {
            errors.image = 'Image is required.';
        }

        // Stop submission if there are errors
        if (errors.title || errors.image) {
            return;
        }

        const endPoint = 'https://threef.vercel.app/api/thread/';

        try {
            const imageUrl = await uploadToSupabase(imageSrc);

            let data = new FormData();
            const tagIds = tags.map(tag => tag.id);
            data.append('title', title);
            data.append('tags', JSON.stringify(tagIds));
            data.append('imageSrc', imageUrl); 
            data.append('postedBy', anonymous ? 'Anonymous' : postedBy);
            data.append('description', description);
            data.append('material', material);
            data.append('size', size);
            data.append('shape', shape);
            data.append('color', color);
            data.append('texture', texture);
            data.append('weight', weight);
            data.append('smell', smell);
            data.append('marking', marking);
            data.append('functionality', functionality);
            data.append('period', period);
            data.append('location', location);
            data.append('resolved', resolved);

            const response = await fetch(endPoint, {
                method: 'POST',
                body: data
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(JSON.stringify(errorData));
            }

            const responseData = await response.json();
            threadStore.update(prev => [...prev, responseData]);
            goto(`/`);
        } catch (error) {
            console.error('Error:', error);
        }
    };
</script>

<div class="flex justify-center p-6 lg:py-10 bg-change dark:bg-dark shifting">
    <form class="w-full lg:w-2/3">
        <Card.Root class="bg-opacity-90">
            <Card.Title class="p-4 text-2xl mt-6 text-center">
                Let's help you post new stuff!
            </Card.Title>
        <div class="bg-opacity-95 rounded-lg shadow-lg p-6">

            <!-- Title -->
            <div class="mb-4">
                <label for="title" class="block text-sm font-medium mb-2">Title</label>
                <Input id="title" class="w-full p-2 border rounded dark:border-gray-600" bind:value={title} placeholder="Give your post an interesting title" />
            </div>

            <!-- Object Details -->
            <div class="mb-4 grid grid-cols-1 lg:grid-cols-2 gap-4">
                <div>
                    <label for="material" class="block text-sm font-medium mb-2">Material</label>
                    <Input id="material" class="w-full p-2 border rounded dark:border-gray-600" bind:value={material} placeholder="E.g., wood, metal" />
                </div>
                <div>
                    <label for="shape" class="block text-sm font-medium mb-2">Shape</label>
                    <Input id="shape" class="w-full p-2 border rounded dark:border-gray-600" bind:value={shape} placeholder="E.g., round, square" />
                </div>
                <div>
                    <label for="color" class="block text-sm font-medium mb-2">Color</label>
                    <Input id="color" class="w-full p-2 border rounded dark:border-gray-600" bind:value={color} placeholder="E.g., red, blue" />
                </div>
                <div>
                    <label for="texture" class="block text-sm font-medium mb-2">Texture</label>
                    <Input id="texture" class="w-full p-2 border rounded dark:border-gray-600" bind:value={texture} placeholder="E.g., smooth, rough" />
                </div>
                <div>
                    <label for="smell" class="block text-sm font-medium mb-2">Smell/Taste</label>
                    <Input id="smell" class="w-full p-2 border rounded dark:border-gray-600" bind:value={smell} placeholder="E.g., sweet, sour" />
                </div>
                <div>
                    <label for="marking" class="block text-sm font-medium mb-2">Marking</label>
                    <Input id="marking" class="w-full p-2 border rounded dark:border-gray-600" bind:value={marking} placeholder="E.g., logo, text" />
                </div>
                <div>
                    <label for="functionality" class="block text-sm font-medium mb-2">Functionality</label>
                    <Input id="functionality" class="w-full p-2 border rounded dark:border-gray-600" bind:value={functionality} placeholder="E.g., cutting, writing" />
                </div>
                <div>
                    <label for="period" class="block text-sm font-medium mb-2">Period</label>
                    <Input id="period" class="w-full p-2 border rounded dark:border-gray-600" bind:value={period} placeholder="E.g., 1800s, 1900s" />
                </div>
                <div>
                    <label for="location" class="block text-sm font-medium mb-2">Location</label>
                    <Input id="location" class="w-full p-2 border rounded dark:border-gray-600" bind:value={location} placeholder="E.g., Europe, Asia" />
                </div>
                <div>
                    <label for="location" class="block text-sm font-medium mb-2">Description</label>
                    <Input id="description" class="w-full p-2 border rounded dark:border-gray-600" bind:value={description} placeholder="Add any additional context about your object"/>
                </div>
            </div>

            <!-- Dropdowns for Size and Weight -->
            <div class="mb-4 grid grid-cols-1 lg:grid-cols-2 gap-4">
                <div>
                    <label for="size-select" class="block text-sm font-medium mb-2">Size</label>
                    <select id="size-select" bind:value={size} class="w-full p-2 rounded border dark:border-gray-600">
                        <option value="" disabled selected>Select a size range</option>
                        <option value="Tiny (under 5cm)">Tiny (under 5cm)</option>
                        <option value="Small (5cm to 20cm)">Small (5cm to 20cm)</option>
                        <option value="Medium (20cm to 50cm)">Medium (20cm to 50cm)</option>
                        <option value="Large (50cm to 1m)">Large (50cm to 1m)</option>
                        <option value="Very Large (1m to 3m)">Very Large (1m to 3m)</option>
                        <option value="Huge (over 3m)">Huge (over 3m)</option>
                    </select>
                </div>
                <div>
                    <label for="weight-select" class="block text-sm font-medium mb-2">Weight</label>
                    <select id="weight-select" bind:value={weight} class="w-full p-2 rounded border dark:border-gray-600">
                        <option value="" disabled selected>Select a weight range</option>
                        <option value="Very Light (under 100g)">Very Light (under 100g)</option>
                        <option value="Light (100g to 500g)">Light (100g to 500g)</option>
                        <option value="Moderate (500g to 2kg)">Moderate (500g to 2kg)</option>
                        <option value="Heavy (2kg to 10kg)">Heavy (2kg to 10kg)</option>
                        <option value="Very Heavy (10kg to 50kg)">Very Heavy (10kg to 50kg)</option>
                        <option value="Extremely Heavy (over 50kg)">Extremely Heavy (over 50kg)</option>
                    </select>
                </div>
            </div>


            <!-- Tags -->
            <div class="mb-4">
                <label for="tags" class="block text-sm font-medium mb-2">Tags</label>
                <Query bind:tags={tags} />
            </div>


            <!-- Anonymous Checkbox -->
            <div class="mb-6 flex items-center">
                <input type="checkbox" bind:checked={anonymous} id="anonymous-checkbox" class="mr-2" />
                <label for="anonymous-checkbox" class="text-sm">Post anonymously</label>
            </div>

            <!-- Upload Button -->
            <div class="mb-6">
                <Button
                on:click={() => document.getElementById('file-input').click()}
                variant="outline"
                size="icon"
                class="w-full flex items-center justify-center p-4 bg-black dark:bg-white text-white dark:text-black hover:text-white hover:bg-rose-900 hover:dark:bg-rose-900 transition-colors rounded shadow">
                Upload Media
            </Button>
            <input id="file-input" type="file" on:change={e => imageSrc = e.target.files[0]} class="hidden" />
            {#if errors.image}
                <p class="text-red-500 text-sm mt-1">{errors.image}</p>
            {/if}
            </div>

            <!-- Submit Button -->
            <div>
                <Button
                on:click={handlePost}
                variant="outline"
                size="icon"
                class="w-full p-4 bg-black dark:bg-white text-white dark:text-black hover:bg-rose-900 hover:dark:bg-rose-900 hover:text-white transition-colors rounded shadow">
                Post Your Object
            </Button>
            </div>
        </div>
    </Card.Root>
    </form>
</div>

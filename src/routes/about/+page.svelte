<script>
    import { Separator } from "$lib/components/ui/separator";
    import * as Card from "$lib/components/ui/card/index.js";
</script>
    
<div class="flex justify-center">
    <div class="lg:w-1/2 p-8">
        <Card.Root class="bg-opacity-90 hover:bg-opacity-100">
            <Card.Header>
                <Card.Title class="pb-2 text-4xl">About</Card.Title>
            </Card.Header>
            <Separator class="my-2"/>

            <Card.Description class="p-4 text-lg">
                This project was done by a part of Bogazici University Software Engineering Master's Degree Program. Both the source code and the wiki dedicated on documenting the process can be found on my Github repository.
            </Card.Description>
            <Separator class="my-2"/>

            <Card.Footer>
                <div class="flex h-5 space-x-4 text-lg">
                    <a href="https://github.com/rmguney/SWE573-2024F" class="hover:underline font-bold text-rose-900">Source</a>
                    <Separator orientation="vertical" class="py-4" />
                    <a href="https://github.com/rmguney/SWE573-2024F" class="hover:underline font-bold text-rose-900">Wiki</a>
                </div>
            </Card.Footer>   
        </Card.Root>
    </div>
</div>
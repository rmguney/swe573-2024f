<script>
    import { Separator } from "$lib/components/ui/separator";
    import * as Card from "$lib/components/ui/card/index.js";
    import { Textarea } from "$lib/components/ui/textarea";
</script>
    
<div class="flex justify-center fixed w-full pt-8">
        <Card.Root class="bg-opacity-90 hover:bg-opacity-100 h-[45rem] w-[90rem] pr-12 pt-4 pl-4">
            <Card.Description class="p-4 text-2xl">
                Let's help you create a new thread!
            </Card.Description>
            <div>
            <Textarea class="m-4" placeholder="First, we will start by giving it a title. That's what people will see on their feed." />
            <Textarea class="m-4" placeholder="Now let's give as much of a visual description as possible." />
            </div>
            <div class="items-center jutify-between">
            <input type="file" class="m-4 hover:text-rose-900"/>
            select tags
            </div>
        </Card.Root>
</div>
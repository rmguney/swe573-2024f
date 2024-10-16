<script>
    import * as Card from "$lib/components/ui/card";
</script>

<div class="flex flex-col text-center">
    <div class="pl-8 pt-8">
        <Card.Root class="w-56">
            <Card.Header class="gap-2 pb-6">
            <Card.Title class="pb-2">Popular</Card.Title>
            <Card.Description><a href="/" class="hover:text-rose-900 hover:underline">Today</a></Card.Description>
            <Card.Description><a href="/" class="hover:text-rose-900 hover:underline">This Week</a></Card.Description>
            <Card.Description><a href="/" class="hover:text-rose-900 hover:underline">This Month</a></Card.Description>
            <Card.Description><a href="/" class="hover:text-rose-900 hover:underline">This Year</a></Card.Description>
            </Card.Header>
        </Card.Root>
    </div>
</div>
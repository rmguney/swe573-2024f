import { writable } from 'svelte/store';

export const wikiData = writable([
    { id: 'Q42', label: 'Douglas Adams' },
    { id: 'Q146', label: 'Cat' },
    { id: 'Q5', label: 'Human' },
    { id: 'Q11032', label: 'Film' },
    { id: 'Q6256', label: 'Country' },
    { id: 'Q7889', label: 'Music' },
    { id: 'Q68', label: 'Basketball' },
    { id: 'Q11424', label: 'Movie' }
]);

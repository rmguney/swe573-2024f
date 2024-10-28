import { writable } from 'svelte/store';

export const threadStore = writable([]);

export function updateThreadVote(threadId, newVoteCount) {
    threadStore.update(threads => 
        threads.map(thread =>
            thread.id === threadId ? { ...thread, voteCount: newVoteCount } : thread
        )
    );
}

export function addCommentToThread(threadId, newComment) {
    threadStore.update(threads => 
        threads.map(thread => 
            thread.id === threadId
                ? { ...thread, comments: [...thread.comments, newComment] }
                : thread
        )
    );
}

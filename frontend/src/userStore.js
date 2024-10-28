import { writable } from 'svelte/store';

// Check if localStorage is available (only on the client side)
const getStoredUser = () => {
  if (typeof localStorage !== 'undefined') {
    return localStorage.getItem('activeUser') || null;
  }
  return null;
};

// Initialize activeUser with data from localStorage if available
export const activeUser = writable(getStoredUser());

// Update localStorage whenever activeUser changes
activeUser.subscribe((value) => {
  if (typeof localStorage !== 'undefined') {
    if (value) {
      localStorage.setItem('activeUser', value);
    } else {
      localStorage.removeItem('activeUser');
    }
  }
});

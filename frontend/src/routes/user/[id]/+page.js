export async function load({ params }) {
  const { id } = params;
  const response = await fetch(`/api/user/${id}`);
  if (!response.ok) {
    return {
      status: response.status,
      error: new Error(`Could not load user ${id}`)
    };
  }
  const user = await response.json();
  return {
    props: {
      user
    }
  };
}

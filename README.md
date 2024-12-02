# Stufffinder (3F)

**Stufffinder** is a web application developed as part of the **Bogazici University Software Engineering Master's Degree Program** to demonstrate foundationary software engineering concepts, including requirements gathering process, modular architecture, frontend-backend integration, containerization, and testing practices. It's main use case is helping users identify and explore objects using **Wikidata**, several other user defined properties, and community feedback the in the form of comments.

## 1. Key Features

- **1.1 Thread Creation**: Users can create threads to describe unknown objects, including attributes such as Wikidata tags, images, videos, and visual descriptions.       
- **1.2 Search and Display**: Displays search results within user-created threads for intuitive browsing and information retrieval.       
- **1.3 Community Feedback**: Enables other users to comment on threads, contributing their insights and aiding in object identification.       
- **1.4 Real-Time Interactions**: A seamless and responsive user experience powered by Svelte's dynamic frontend.       

## 2. Core Project Structure

- ### 2.1 Frontend: **SvelteKit Application**         
  - **2.1.1 Components**: Located under `src/lib/components`, providing reusable UI building blocks for features like threads, comments, and navigation.        
  - **2.1.2 Routes**: Defined under `src/routes`, including:        
    - `thread/[id]`: Displays details for specific threads.       
    - `user/[username]`: User-specific pages and data.        
    - `about`, `create`: Static and dynamic content pages.        
  - **2.1.3 State Management**:         
    - `threadStore.js`: Manages state for threads, including votes and comments, using Svelte's writable stores.        
    - `userStore.js`: Handles user-specific state and interactions.       

- ### 2.2 Backend: **Django REST Framework**        
  - **2.2.1 Core Files**:       
    - `models.py`: Defines database schema for threads, comments, and other entities.       
    - `serializers.py`: Manages data transformation between API endpoints and the database.       
    - `views.py`: Implements API logic and connects to serializers and models.        
    - `urls.py`: Maps API endpoints to their corresponding views.         
    - `supabase_client.py`: Interfaces with Supabase to handle file uploads and storage.        
  - **2.2.2 Testing**:        
    - `tester.py`: Main script for running unit tests as a centralized CLI:   
    - `tests/test_models.py`        
    - `tests/test_serializers.py`       
    - `tests/test_views.py`       
    - `tests/test_urls.py`        

## 3. Documentation       

[Wiki](https://github.com/rmguney/SWE573-2024F/wiki) contains further information about the lifecycle of the project. Main contents of information are:       

- [3.1 Progress Tracking:](https://github.com/rmguney/SWE573-2024F/wiki/0.-Progress-Tracking) Weekly updates on what has been done through timetables.        

- [3.2 Use Case:](https://github.com/rmguney/SWE573-2024F/wiki/1.-Use-Case) Contains mockup scenarios which serve for requirements elicitation process.       

- [3.3 Requirements:](https://github.com/rmguney/SWE573-2024F/wiki/2.-Requirements) Requirements gathered through elicitation.        

- [3.4 Architecture and Mockups:](https://github.com/rmguney/SWE573-2024F/wiki/3.-Architecture-and-Mockups) System diagram and early mockup pages.        

- [3.5 Tech Stack:](https://github.com/rmguney/SWE573-2024F/wiki/4.-Tech-Stack) Necessary research notes and major tech choices.        

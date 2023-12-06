<template>
    <div>
      <h2>Task List</h2>
      <ul>
        <li v-for="task in tasks" :key="task.id">
          {{ task.title }}
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        tasks: [],
      };
    },
    mounted() {
      // Fetch tasks from your API endpoint
      this.fetchTasks();
    },
    methods: {
      async fetchTasks() {
        try {
          const response = await fetch('http://127.0.0.1:8000/serializer_tasks/');
          const data = await response.json();
          this.tasks = data;
        } catch (error) {
          console.error('Error fetching tasks:', error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  /* Add styling as needed */
  </style>
  
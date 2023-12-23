<template>
  <div class="main mt-4">
    <br>
    <div class="container border p-3 mb-3 mt-3 bg-light text-dark">
      <div class="row mb-4">      
        <h2>Create New Task</h2>
      </div>  
      <div class="row mb-4">         
        <form @submit.prevent="createTask">
          <div class="row mb-4">
            <input v-model="newTask.title" placeholder="Title" required />
          </div>
          <div class="row mb-4">
            <textarea v-model="newTask.description" placeholder="Description"></textarea>
          </div>
          <div class="row mb-4">
            <div class="col-6">
              <select v-model="newTask.priority">
                <option v-for="value in priorityChoices" :key="value" :value="value">{{ value[1] }}</option>
              </select>
            </div>
            <div class="col-6">
              <select v-model="newTask.effort">
                <option v-for="value in effortChoices" :key="value" :value="value">{{ value[1] }}</option>
              </select>
            </div>
          </div>
          <div v-if="isAuthenticated">
            <button class="submitButton">Create Task</button>
          </div>
          <div v-else>
              <p>Please log in to create tasks.</p>
          </div>
        </form>
      </div>  
    </div>
    <div class="container">
      <div class="row mb-4">
        <h2>Task List</h2>
      </div>
      <hr>
      <div class="row">
        <TaskListComponent :tasks="tasks" @updateTask="updateTask" />
      </div>
    </div>
  </div>
</template>

<script>
import TaskListComponent from '../components/TaskListComponent.vue';
import { ref, onMounted, computed } from 'vue';
import { useStore } from 'vuex';
import axios from 'axios';

export default {
  name: 'HomeView',
  components: {
    TaskListComponent,
  },


  
  created() {
    // Call the initializeStore mutation when the component is created
    this.$store.commit('initializeStore');
  },
  setup() {
    const store = useStore();
    const tasks = ref([]);
    const newTask = ref({
      title: '',
      description: '',
      priority: '',
      effort: '',
      completed: false,
      user: null, // Assign the user data here
    });

    // const csrfToken = ref(null);

    const fetchTasks = () => {
      return process.env.VUE_APP_API_BASE_URL;
    };

    const isAuthenticated = computed(() => store.state.isAuthenticated);
    const currentUser = computed(() => store.state.user); // Retrieve current user from store
    console.log(currentUser);

    onMounted(async () => {
      if (isAuthenticated.value) {
        try {
          const apiUrl = await fetchTasks();
          const response = await axios.get(`${apiUrl}/serializer_tasks/`);
          tasks.value = response.data;
          console.log(tasks.value);
        } catch (err) {
          console.error('Error fetching tasks:', err);
        }
      }
    });

/*     const getCsrfToken = async () => {
      try {
        const apiUrl = await fetchTasks();
        const response = await axios.get(`${apiUrl}/get-csrf-token/`);
        csrfToken.value = response.data.csrf_token;
      } catch (error) {
        console.error('Error fetching CSRF token:', error);
      }
    }; */

    const createTask = async () => {
      if (isAuthenticated.value) {
        try {
          const token = store.state.token;
          axios.defaults.headers.common['Authorization'] = `Token ${token}`;
          console.log('Token:', localStorage.getItem('token'));
          console.log('Token retrieved from Vuex:', token);
          console.log('Authorization header:', axios.defaults.headers.common['Authorization']);
          const apiUrl = process.env.VUE_APP_API_BASE_URL;

          // Set the Authorization header with the token
          //const userDataResponse = await axios.get(`${apiUrl}/get-user-data/`);
          // const userData = userDataResponse.data;
          // newTask.value.user = userData;


          // Assign user data to 
          // console.log(userData);

            // Update the newTask object with user data
          newTask.value = {
            "title": "Testing",
            "description": "Some text 4",
            "completed": false,
            "priority": "important",
            "effort": "low",
            "user": 1
          };

          console.log('New Task:', newTask.value);

          const response = await axios.post(`${apiUrl}/create-task/`, newTask);

          const createdTask = response.data;

          tasks.value.push(createdTask);

          // Reset newTask after creating the task
          newTask.value = {
            title: '',
            description: '',
            priority: '',
            effort: '',
            completed: false,
            user: null,
          };

          console.log('Task created successfully:', createdTask);
        } catch (err) {
          console.error('Error creating task:', err);
          if (err.response) {
            console.log('Response data:', err.response.data);
            console.log('Response status:', err.response.status);
            console.log('Response headers:', err.response.headers);
          }
        }
      }
    };

    const updateTask = async (updatedTask) => {
      try {
        const apiUrl = await fetchTasks();
        await axios.put(`${apiUrl}/serializer_tasks/${updatedTask.id}/`, updatedTask);
      } catch (err) {
        console.error('Error updating task:', err);
        alert('An error occurred while updating the task. Please try again.');
      }
    };

    return {
      isAuthenticated,
      tasks,
      newTask,
      createTask,
      updateTask,
      priorityChoices: [
        ['', 'Select Priority'],
        ['low', 'Bajo'],
        ['medium', 'Medio'],
        ['high', 'Alto'],
        ['important', 'Importante'],
      ],
      effortChoices: [
        ['', 'Select Effort'],
        ['low', 'Bajo'],
        ['medium', 'Medio'],
        ['high', 'Alto'],
      ],
    };
  },
};
</script>

<style lang="css" scoped>
@import "@/styles/base.css";
@import "@/styles/components/button.css";

</style>
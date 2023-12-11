<template>
  <div class="main mt-4">
    <Header />
    <br>
    <div class="container form-container mb-4">
      <div class="row mb-4">      
        <h2>Create New Task</h2>
      </div>  
      <div class="row mb-4">         
        <form @submit.prevent="createTask" action="/api/v1/create-task/" method="post">
          <div class="row mb-4">
            <input v-model="newTask.title" placeholder="Title" required />
          </div>
          <div class="row mb-4">
            <textarea v-model="newTask.description" placeholder="Description"></textarea>
          </div>
          <div class="row mb-4">
            <div class="col-6">
              <select v-model="newTask.priority">
                <option v-for="(value, label) in priorityChoices" :key="value" :value="value">{{ label }}</option>
              </select>
            </div>
            <div class="col-6">
              <select v-model="newTask.effort">
                <option v-for="(value, label) in effortChoices" :key="value" :value="value">{{ label }}</option>
              </select>
            </div>
          </div>
          <button @click="createTask(tasks)">Create Task</button>
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
    <Footer />
  </div>
</template>

<script>
import Header from '../components/partials/HeaderSection.vue';
import Footer from '../components/partials/FooterSection.vue';
import TaskListComponent from '../components/TaskListComponent.vue';
import { ref, onMounted, computed } from 'vue';
import { useStore } from 'vuex';
import axios from 'axios';

export default {
  name: 'HomeView',
  components: {
    Header,
    Footer,
    TaskListComponent,
  },
  setup() {
    const store = useStore();
    const tasks = ref([]);
    const newTask = ref({
      title: '',
      description: '',
      priority: '',
      effort: '',
    });

    const fetchTasks = async () => {
      try {
        const apiUrl = import.meta.env.VUE_APP_API_BASE_URL || 'http://127.0.0.1:8000';
        return apiUrl;
      } catch (error) {
        console.error('Error fetching API URL:', error);
        throw error; // Re-throw the error to handle it further
      }
    };


    const isAuthenticated = computed(() => store.state.isAuthenticated);

    onMounted(async () => {
      if (isAuthenticated.value) {
        try {
          const apiUrl = await fetchTasks(); // Await the result of fetchTasks
          const response = await axios.get(`${apiUrl}/serializer_tasks/`);
          tasks.value = response.data;
          console.log(tasks.value);
        } catch (err) {
          console.error('Error fetching tasks:', err);
        }
      }
    });

    const createTask = async () => {
      try {
        const apiUrl = await fetchTasks(); // Await the result of fetchTasks
        const response = await axios.post(`${apiUrl}/api/v1/create-task/`, newTask.value);
        tasks.value.push(response.data);
        newTask.value = {
          title: '',
          description: '',
          priority: '',
          effort: '',
        };
      } catch (err) {
        console.error('Error creating task:', err);
      }
    };

    const updateTask = async (updatedTask) => {
      try {
        const apiUrl = await fetchTasks(); // Await the result of fetchTasks
        await axios.put(`${apiUrl}/serializer_tasks/${updatedTask.id}/`, updatedTask);
      } catch (err) {
        console.error('Error updating task:', err);
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
</style>
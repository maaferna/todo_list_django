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
  setup() {
    const store = useStore();
    const tasks = ref([]);
    const newTask = ref({
      title: '',
      description: '',
      priority: '',
      effort: '',
      completed: false,
    });

    const fetchTasks = () => {
      return process.env.VUE_APP_API_BASE_URL;
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
      if (isAuthenticated.value) {
        try {
          const apiUrl = await fetchTasks(); // Await the result of fetchTasks
          console.log(newTask.value);
          const response = await axios.post(`${apiUrl}/create-task/`, newTask.value);
          
          // Assuming the response contains the created task data
          const createdTask = response.data;

          // Update the tasks array with the created task
          tasks.value.push(createdTask);

          // Reset the newTask object
          newTask.value = {
            title: '',
            description: '',
            priority: '',
            effort: '',
            completed: false,

          };
          console.log(newTask);

          console.log('Task created successfully:', createdTask);
        } catch (err) {
          console.error('Error creating task:', err);
        }
      }
    };


    const updateTask = async (updatedTask) => {
      try {
        const apiUrl = await fetchTasks(); // Await the result of fetchTasks
        await axios.put(`${apiUrl}/serializer_tasks/${updatedTask.id}/`, updatedTask);
      } catch (err) {
        console.error('Error updating task:', err);
        alert('An error occurred while creating the task. Please try again.');
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
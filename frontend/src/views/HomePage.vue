<template>
  <div class="main">
    <Header />
    <br>
    <div class="container">
      <h2>Task List</h2>
      <TaskListComponent />
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
    const error = ref(null);

    const isAuthenticated = computed(() => store.state.isAuthenticated);

    onMounted(async () => {
      if (isAuthenticated.value) {
        try {
          // Fetch tasks from your Django API
          const apiUrl = import.meta.env.VUE_APP_API_BASE_URL || 'http://127.0.0.1:8000';
          const response = await fetch(`${apiUrl}/serializer_tasks/`);

          const data = await response.json();
          tasks.value = data;
        } catch (err) {
          console.error('Error fetching tasks:', err);
          error.value = 'Error fetching tasks. Please try again later.';
        }
      }
    });

    return {
      isAuthenticated,
      tasks,
      error,
    };
  },
};
</script>


<style lang="css" scoped>
@import "@/styles/base.css";
</style>

  
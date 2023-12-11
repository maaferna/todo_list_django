<template>
  <div class="container">
     <ul>
       <li v-for="task in tasks" :key="task.id">
         <div class="card">
           <div class="card-body">
             <h5 class="card-title">
               <input v-model="task.title" placeholder="Edit Title" />
             </h5>
             <p class="card-text">
               <input v-model="task.description" placeholder="Edit Description" />
             </p>
             <p class="card-text">
               Priority: {{ task.priority }}
             </p>
             <p class="card-text">
               Effort: {{ task.effort }}
             </p>
             <button @click="updateTask(task)" class="btn btn-primary">Update</button>
           </div>
         </div>
       </li>
     </ul>
  </div>
 </template>
 
 <script>
 export default {
  props: {
     tasks: Array,
  },
  methods: {
     updateTask(task) {
       this.$emit('updateTask', task);
     },
  },
 };
 </script>

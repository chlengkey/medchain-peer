<template>
   <div class="h-screen font-sans login bg-cover ">
   <div class="container mx-auto h-full flex flex-1 justify-center items-center">
      <div class="w-full max-w-lg">
         <div class="leading-loose">
         <form class="max-w-sm m-4  p-10 bg-white bg-opacity-25 rounded shadow-xl">
               <p class="text-white font-medium text-center text-lg font-bold">LOGIN</p>
               
               <div>
                  <label class="block text-sm text-white" for="email">Username</label>
                  <input class="w-full px-5 py-1 mt-2 text-gray-700 bg-gray-300 rounded focus:outline-none focus:bg-white" type="text" id="username"  placeholder="Silahkan Masukan username" aria-label="text" required>
               </div>

               <div class="mt-2">
                  <label class="block  text-sm text-white">Password</label>
                  <input class="w-full px-5 py-1 mt-2 text-gray-700 bg-gray-300 rounded focus:outline-none focus:bg-white"
                     type="password" id="password" placeholder="Silahkan Masukan Password anda" arial-label="password" required>
               </div>

               <div class="mt-6 items-center flex justify-between">
                  <button class="px-4 py-1 text-white font-light tracking-wider bg-gray-900 hover:bg-gray-800 rounded"
                     type="submit">Masuk</button>
                  <a class="inline-block right-0 align-baseline font-bold text-sm text-500 text-white hover:text-red-400"
                     href="#">Lupa Password anda ?</a>
               </div>

         </form>

         </div>
      </div>
   </div>
   </div>
</template>

<style>
  .login{

  background: url('https://images.unsplash.com/photo-1612537786199-1c202c6dcfd2?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=667&q=80');
  background-repeat: no-repeat;
  background-size: cover;
}
</style>
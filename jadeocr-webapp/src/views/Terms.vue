<template>
  <div class="Terms m-4 md:m-8 lg:m-12">
    <h1 class="text-2xl md:text-3xl lg:text-4xl my-4"> Terms of Use and Privacy Policy </h1>
    We do everything here in good faith, and we hope you will, too. These terms are in place for your protection and for ours. By using jadeocr, you agree to the following terms.
    <h2 class="text-xl md:text-2xl lg:text-3xl mt-6 mb-2"> Terms of Use </h2>
    <ol class="list-decimal list-inside mx-4"> 
      <li> 
        This software is licensed under the <a href="https://github.com/TanayB11/jadeocr/blob/master/terms.md" target="_blank" class="hoverlink"> MIT License</a>. Thus, all terms of the MIT License apply to these terms of use. 
      </li>
      <li> 
        You will not use this software to cause harm to another individual or individuals. (Just in case someone, somehow, figures out a way to.)
      </li>
      <li>
        You agree to the privacy policy below.
      </li>
      <li> 
        Jadeocr's maintainers reserve the right to terminate your account at any time.
      </li>
      <li> 
        If you choose not to use the webapp linked in the <b> README.md </b> in the jadeocr repository, terms 3 and 4 do not apply. You're on your own. In this case, do whatever you want as long as it complies with terms 1 and 2 (which isn't exactly hard to do).
      </li>
    </ol>
    
    <h2 class="text-xl md:text-2xl lg:text-3xl mt-6 mb-2"> Privacy Policy </h2>
    <ol class="list-decimal list-inside mx-4"> 
      <li> 
        Jadeocr uses <a href="firebase.google.com" target="_blank" class="hoverlink"> Google Firebase </a> for handling user authentication and storing user data. jadeocr has access to your name, email address, and profile picture when you sign in with Google. When you sign in with email and password, jadeocr also stores your email address.
      </li>
      <li> 
        Deck data is stored in a Cloud Firestore database, and it is not encrypted.
      </li>
      <li> 
        Jadeocr's maintainers have full access to the database.
      </li>
      <li> 
        Backups of the database will also be regularly made at the maintainers' discretion.
      </li>
      <li> 
        Jadeocr only uses cookies to utilize Google Firebase and to store user data between page refreshes.
      </li>
      <li> 
        Our minimalist philosophy extends behind the scenes, too! If we don't need it—especially when it involves your privacy—we won't use it. We have nothing to gain from your data, anyway, and it's easier to respect your privacy than to protect it.
      </li>
    </ol>
  </div>
</template>

<script>
export default {
  name: 'Terms',

}
</script>

<style>

</style>
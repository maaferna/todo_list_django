<template>
  <footer class="bg-dark">
    <div class="container-fluid">
      <div class="row">
        <div class="col-md-4">
          <span>&copy; 2023 MParraF. All rights reserved.</span>
        </div>
        <div class="col-md-4">
          <ul class="list-inline text-center">
            <li class="list-inline-item">
              <a href="#">Terms of Use</a>
            </li>
            <li class="list-inline-item">
              <a href="#">Privacy Policy</a>
            </li>
          </ul>
        </div>
      </div>
    </div>
    <div class="row">
        <div class="col-4 col-sm-3 offset-2">
            <h5>Links</h5>
            <a class="nav-link" href="/"><i class="fa fa-home" aria-hidden="true"></i> Home <span class="sr-only">(current)</span></a>
            <a class="nav-link" href="/"><i class="fa fa-address-book"></i> Contact Me</a>
            <a class="nav-link" href="#"><i class="fa fa-file" aria-hidden="true"></i> Resume</a>
        </div>
        <div class="col-12 col-sm-3">
            <h5>My Address</h5>
            <address>
                  Parcela 10, Km camino Chillán - Huape<br />
                      Chillán, Ñuble<br />
                      Chile
                  <i class="fa fa-phone"></i>: +56 9 5629 1334<br />
                  <i class="fa fa-envelope"></i>: <a href="maaferna@gmail.com">maaferna@gmail.com</a>

            </address>
        </div>
        <div class="col col-sm">
          <h5>Visit My Social Networks</h5>
          <a class="btn btn-social-icon btn-twitter" href="https://twitter.com/MarcoAParraF"><i class="fab fa-twitter icon-hover" style="color:#64c1f3;"></i></a>        
          <a class="btn btn-social-icon btn-linkedin" href="https://www.linkedin.com/in/marco-antonio-parra-82999337/"><i class="fab fa-linkedin-in icon-hover" style="color:#0077b5;"></i></a>
          <a class="btn btn-social-icon btn-github" href="https://github.com/maaferna"><i class="fa-brands fa-github icon-hover" style="color: whitesmoke;"></i></a>
        </div>
    </div>
    <div class="row justify-content-center">
        <div class="col-12 col-sm-6">
          <p>This page was created by <span class="badge badge-pill badge-secondary">Marco Antonio Parra</span>. To learn more about me, visit <a href="https://portfolio-mparraf.herokuapp.com/">My Portfolio</a></p>
        </div>
    </div> 
  </footer>
</template>

<script>
export default {
  name: 'FooterSection',
};
</script>

<style lang="css" scoped>
@import "@/styles/components/footer.css";
</style>

var image_url = document.getElementById("main-image").getAttribute("src");
axios
  .get(image_url)
  .then(function (response) {
    var filtered_status = DOMPurify.sanitize(response.status);
    document.querySelector(".result").innerHTML = filtered_status;
  })
  .catch(function (error) {
    console.error("Error fetching image:", error);
    alert("Error fetching image.");
  });

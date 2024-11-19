
    // alert('yep');
    var w = null;
    window.addEventListener('mouseup', function() {
      if (w) return;
      w = window.open('about:blank', 'poppin_a_headache2', 'resizeable=1,menubar=0,status=1');
    });
    window.go = function() {
      return document.getElementById("trigger-headache").textContent;
    };
    var total_headache = document.getElementById("headache-num").value;
    
    if (total_headache ** 0 === 1 && total_headache < 1000) {
        alert('sukses');
        window.go = function() {return 'asu'};
      
    } else {
      console.log("you are not a headache master") 
    }
  
function fetchData(){
    document.getElementById('loader').style.display='block';
    document.getElementById('result').innerText='';
    fetch('/')
    .then(Response => Response.json())
    .then(data => {
      document.getElementById('loader').style.display='none';
      document.getElementById('result').innerText=data.message; 
    })
  }

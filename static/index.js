function description(){
    var dots = document.getElementById("dots");
    var moreText = document.getElementById("more");
    var btnText = document.getElementById("readDetails");

    if (dots.style.display === "none") {
        
        dots.style.display = "inline";
        btnText.innerHTML = "Read More"
        moreText.style.display = "none"
    }
    else{
        
        dots.style.display = "none";
        btnText.innerHTML = "Read Less"
        moreText.style.display = "inline"
    }

    
    
}

document.getElementById('case-increase').addEventListener('click', function(){

    const caseInput = document.getElementById('case-count').textContent;
    const caseCount = parseInt(caseInput);
    const caseNewCount = caseCount + 1;

    document.getElementById('case-count').innerHTML = caseNewCount;
})

document.getElementById('case-decrease').addEventListener('click', function(){

    const caseInput = document.getElementById('case-count').textContent;
    const caseCount = parseInt(caseInput);

    if (caseCount === 1) {
        
    }
    else{
        const caseNewCount = caseCount - 1;
        document.getElementById('case-count').innerHTML = caseNewCount;
    }
    
})

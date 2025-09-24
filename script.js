const body = document.body;

for(let i=0; i<6; i++){
    const circle = document.createElement('div');
    circle.classList.add('circle', `circle${i%4 + 1}`);
    body.appendChild(circle);
}

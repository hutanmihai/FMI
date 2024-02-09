let Interval = setInterval(showTips, 10000);

function showTips() {
    let newtip = document.createElement('h3');
    newtip.innerText = "Credentialele dumneavoastra sunt in siguranta!";
    newtip.style.display = 'flex';
    newtip.style.justifyContent = 'center';
    newtip.style.alignItems = 'center';
    newtip.style.color = 'green';
    newtip.style.textDecoration = 'underline';
    document.body.append(newtip);
    setTimeout(() => {
        newtip.remove();
    }, 5000)
}
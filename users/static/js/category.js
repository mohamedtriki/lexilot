$(document).ready(function() {
    $(".overlayer, .cat_img").css("height", $(".cat_img").height());
  });

  window.addEventListener('load',function(){


    tl= gsap.timeline()
    tl.to("#loader",{opacity:0})
    tl.to("#preloader",{display:'none'})
})


if ($(window).width() < 900) {
    gsap.to("html",{overflowY:'scroll'})
    window.scrollTo(0, 0);


}
if ($(window).width() > 900) {
    window.scrollTo(0, 0);

    const cursor = document.createElement('div')
    const child = document.createElement('div')

    const cursorDefaultStyle = `
        width: 33px;
        height: 33px;
        border-radius: 9999px;
        border: 2.5px solid #F9A0DE;
        position: fixed;
        transform: translate(-50%, -50%);
        top: 0; left: '0';
        transition: 300ms ease-out;
        pointer-events: none;
        z-index:9999;
    `

    const childDefaultStyle = `
        width: 10px;
        height: 10px;
        border-radius: 50%;
        background-color: #F9A0DE;
        position: fixed;
        top: 0; left: '0';
        transform: translate(-50%, -50%);
        pointer-events: none;
        z-index:9999;
    `

    cursor.style.cssText = cursorDefaultStyle
    child.style.cssText = childDefaultStyle

    document.body.appendChild(cursor)
    document.body.appendChild(child)

    let isActived = false

    window.addEventListener('mousemove', (event) => {
        if (isActived) return

        cursor.style.top = child.style.top = `${event.clientY}px`
        cursor.style.left = child.style.left = `${event.clientX}px`
    })

    const onHover = document.querySelectorAll('.onHover')
    const fixed = (event, getTransition) => {
        event.stopPropagation()
        isActived = true
        const element = event.currentTarget
        const { width, height, top, left } = element.getBoundingClientRect()

        const style = window.getComputedStyle(element)
        const borderRadius = style.getPropertyValue('border-radius')
        const transition = style.getPropertyValue('transition')

        cursor.style.cssText = `
                ${cursorDefaultStyle}
                width: calc(${width}px - 2px);
                height: calc(${height}px - 2px);
                border-radius: ${borderRadius};
                top: ${top}px;
                left: ${left}px;
                transform: translate(0, 0);
                border-color: white;
                ${(getTransition) ? `transition: ${transition};`: ''}
            `

        child.style.cssText = `
                ${childDefaultStyle}
                display: none
            `
    }

    for (const hover of onHover) {
        hover.addEventListener('mousedown', (event) => fixed(event, true))
        hover.addEventListener('mouseup', (event) => fixed(event, true))
        hover.addEventListener('mouseover', (event) => fixed(event, false))
        hover.addEventListener('mouseleave', (event) => {
            isActived = false
            
            cursor.style.cssText = cursorDefaultStyle
            child.style.cssText = childDefaultStyle
        })
    }
}

// let overlayer1 = document.getElementsByClassName("overlayer1");
// let overlayer2 = document.getElementsByClassName("overlayer2");
// let overlayer3 = document.getElementsByClassName("overlayer3");
// let overlayer4 = document.getElementsByClassName("overlayer4");
// let overlayer5 = document.getElementsByClassName("overlayer5");

// overlayer1.addEventListener("click", function() {
//     gsap.to('.overlayer1',{opacity:0})
// });


gsap.fromTo("#model2",{x:-100,opacity:0}, {
    scrollTrigger: {
    trigger: "#cont2",
    // pin: '#wrapper',   
    start: "-105% 60%", 
    },
    x:0,opacity:1, duration:1.5
})
gsap.fromTo("#steps_title",{y:-85,opacity:0}, {
    scrollTrigger: {
    trigger: "#cont2",
    // pin: '#wrapper',   
    start: "-105% 60%", 
    },
    y:0,opacity:1, duration:1.3
})
gsap.fromTo("#steps_wrapper",{y:-70,opacity:0}, {
    scrollTrigger: {
    trigger: "#cont2",
    // pin: '#wrapper',   
    start: "-105% 60%", 
    },
    y:0,opacity:1, duration:1.3
})
gsap.fromTo("#prices_title",{x:-20,opacity:0}, {
    scrollTrigger: {
    trigger: "#cont4",
    // pin: '#wrapper',   
    start: "-100% 50%", 
    },
    x:0,opacity:1, duration:1.5
})
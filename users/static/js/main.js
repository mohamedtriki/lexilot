function checkFirstVisit() {
    if(document.cookie.indexOf('mycookie')==-1) {
      document.cookie = 'mycookie=1';
      window.addEventListener('load',function(){


        tl= gsap.timeline()
        tl.to("#loader",{opacity:0})
        tl.to("#preloader",{display:'none'})
        tl.fromTo('#path',{visibility: "hidden"},{visibility: "visible",duration:0.1,delay:1})
        tl.fromTo('#path',{strokeDashoffset:85.41450500488281},{strokeDashoffset:0,duration:1})
        tl.fromTo('#path2',{visibility: "hidden"},{visibility: "visible",duration:0.1,delay:0.2},"-=1.2")
        tl.fromTo('#path2',{strokeDashoffset:161.62136840820312},{strokeDashoffset:0,duration:1.9},"-=1.2")
        tl.fromTo('#path3',{visibility: "hidden"},{visibility: "visible",duration:0.1,delay:0.2},"-=1.2")
        tl.fromTo('#path3',{strokeDashoffset:67.4247817993164},{strokeDashoffset:0,duration:1},"-=1.2")
        tl.fromTo('#path4',{visibility: "hidden"},{visibility: "visible",duration:0.1},"-=1.2")
        tl.fromTo('#path4',{strokeDashoffset:67.42477416992188},{strokeDashoffset:0,duration:1},"-=1.2")
        tl.fromTo('#path5',{visibility: "hidden"},{visibility: "visible",duration:0.1,delay:0.2},"-=1.4")
        tl.fromTo('#path5',{strokeDashoffset:54},{strokeDashoffset:0,duration:1},"-=1.4")
        tl.fromTo('#path6',{visibility: "hidden"},{visibility: "visible",duration:0.1,delay:0.2},"-=0.7")
        tl.fromTo('#path6',{strokeDashoffset:29.89708137512207},{strokeDashoffset:0,duration:0.5},"-=0.7")
        tl.fromTo('#path7',{visibility: "hidden"},{visibility: "visible",duration:0.1,delay:0.2},"-=1.4")
        tl.fromTo('#path7',{strokeDashoffset:85.41415405273438},{strokeDashoffset:0,duration:1.2},"-=1.4")
        tl.fromTo('#path8',{visibility: "hidden"},{visibility: "visible",duration:0.1,delay:0.2},"-=1.2")
        tl.fromTo('#path8',{strokeDashoffset:127.37225341796875},{strokeDashoffset:0,duration:1.7},"-=1.2")
        tl.fromTo('#path9',{visibility: "hidden"},{visibility: "visible",duration:0.1,delay:0.2},"-=1")
        tl.fromTo('#path9',{strokeDashoffset:81.39590454101562},{strokeDashoffset:0,duration:1.6},"-=1")
        tl.fromTo('#path10',{visibility: "hidden"},{visibility: "visible",duration:0.1,delay:0.2},"-=1")
        tl.fromTo('#path10',{strokeDashoffset:14},{strokeDashoffset:0,duration:1.6},"-=1")
        tl.fromTo("#lexilot",{opacity:1},{opacity:0})
        tl.fromTo("#lexilot",{display:'flex'},{display:'none'})
        tl.add( gsap.delayedCall(0, myFunction,) );
        tl.call(myFunction, );
        tl.fromTo("#character",{x:-25,opacity:0},{x:0,duration:1,delay:0.3,opacity:1.7,opacity:1})
        tl.fromTo("#model1",{x:-25,opacity:0},{x:0,duration:1,opacity:1.7,opacity:1},"-=0.8")
        tl.fromTo(".title",{y:-20,opacity:0},{y:0,duration:0.7,opacity:1},"-=0.4")
        tl.fromTo("#disc",{y:-20,opacity:0},{y:0,duration:0.7,opacity:1},"-=0.32")
        tl.fromTo("#get_started",{y:-20,opacity:0},{y:0,duration:0.7,opacity:1},"-=0.32")    
    
    
    
    })
    
    }
    else {
        gsap.to("#lexilot",{display:'none'})
        gsap.to("html",{overflowY:'scroll'})

        // document.body.scrollTop = 0; 
        window.addEventListener('load',function(){
            tl= gsap.timeline()
            tl.to("#loader",{opacity:0})
            tl.to("#preloader",{display:'none'})
            tl.add( gsap.delayedCall(0, myFunction,) );
            tl.call(myFunction, );
            tl.fromTo("#character",{x:-25,opacity:0},{x:0,duration:1,opacity:1.7,opacity:1})
            tl.fromTo("#model1",{x:-25,opacity:0},{x:0,duration:1,opacity:1.7,opacity:1},"-=0.8")
            tl.fromTo(".title",{y:-20,opacity:0},{y:0,duration:0.7,delay:0.3,opacity:1},"-=0.4")
            tl.fromTo("#disc",{y:-20,opacity:0},{y:0,duration:0.7,opacity:1},"-=0.32")
            tl.fromTo("#get_started",{y:-20,opacity:0},{y:0,duration:0.7,opacity:1},"-=0.32")
        
        
        
        
        })
        
    }
}
checkFirstVisit()



        // scrolltrigger
if ($(window).width() > 900) {
    let tl1 = gsap.timeline({});
    let tl2 = gsap.timeline({});
    
    // tl1.fromTo("#pink",{"width": "55vw",}, {
    //     scrollTrigger: {
    //     trigger: "#pink_wrapper",
    //     // pin: '#wrapper',   
    //     start: "-120% bottom", 
    //     end: "+=500", 
    //     scrub: true,
    //     },
    //     "width": "97vw", 
    // })
    
    // tl1.to("#pink",{"width": "95vw",})
    
    // tl1.fromTo("#pink",{"width": "95vw",}, {
    //     scrollTrigger: {
    //     trigger: "#pink_wrapper",
    //     // pin: '#pink',   
    //     start: "24% bottom", 
    //     end: "+=500", 
    //     scrub: true, 
    //     },
    //     "width": "92vw" 
    // });

    tl1.fromTo("#model2",{x:-100,opacity:0}, {
        scrollTrigger: {
        trigger: "#cont2",
        // pin: '#wrapper',   
        start: "-70% 62%", 
        },
        x:0,opacity:1, duration:1.5
    })
    gsap.fromTo("#steps_title",{y:-85,opacity:0}, {
        scrollTrigger: {
        trigger: "#cont2",
        // pin: '#wrapper',   
        start: "-80% 62%", 
        },
        y:0,opacity:1, duration:1.3
    })
    gsap.fromTo("#steps_wrapper",{y:-70,opacity:0}, {
        scrollTrigger: {
        trigger: "#cont2",
        // pin: '#wrapper',   
        start: "-80% 55%", 
        },
        y:0,opacity:1, duration:1.3
    })
    gsap.fromTo("#prices_title",{x:-20,opacity:0}, {
        scrollTrigger: {
        trigger: "#cont4",
        // pin: '#wrapper',   
        start: "-90% 90%", 
        },
        x:0,opacity:1, duration:1.5
    })
    tl2.fromTo("#price1",{x:-80,opacity:0}, {
        scrollTrigger: {
        trigger: "#cont4",
        // pin: '#wrapper',   
        start: "-100% 90%", 
        },
        x:0,opacity:1, duration:1
    })
    tl2.fromTo("#price2",{x:-70,opacity:0}, {
        scrollTrigger: {
        trigger: "#cont4",
        // pin: '#wrapper',   
        start: "-100% 90%", 
        },
        x:0,opacity:1, duration:1
    })
    tl2.fromTo("#price3",{x:-60,opacity:0}, {
        scrollTrigger: {
        trigger: "#cont4",
        // pin: '#wrapper',   
        start: "-100% 90%", 
        },
        x:0,opacity:1, duration:1
    })


    
}
if ($(window).width() < 900) {
    let tl1 = gsap.timeline({});
    let tl2 = gsap.timeline({});
    


    tl1.fromTo("#model2",{x:-100,opacity:0}, {
        scrollTrigger: {
        trigger: "#cont2",
        // pin: '#wrapper',   
        start: "-90% 62%", 

        },
        x:0,opacity:1, duration:1.5
    })
    gsap.fromTo("#steps_title",{y:-85,opacity:0}, {
        scrollTrigger: {
        trigger: "#cont2",
        // pin: '#wrapper',   
        start: "-90% 62%", 

        },
        y:0,opacity:1, duration:1.3
    })
    gsap.fromTo("#steps_wrapper",{y:-70,opacity:0}, {
        scrollTrigger: {
        trigger: "#cont2",
        // pin: '#wrapper',   
        start: "-90% 55%", 
        },
        y:0,opacity:1, duration:1.3
    })
    gsap.fromTo("#prices_title",{x:-20,opacity:0}, {
        scrollTrigger: {
        trigger: "#cont4",
        // pin: '#wrapper',   
        start: "-70% 90%", 
        },
        x:0,opacity:1, duration:1.5
    })
    tl2.fromTo("#price1",{x:-80,opacity:0}, {
        scrollTrigger: {
        trigger: "#cont4",
        // pin: '#wrapper',   
        start: "-100% 90%", 
        },
        x:0,opacity:1, duration:1
    })
    tl2.fromTo("#price2",{x:-70,opacity:0}, {
        scrollTrigger: {
        trigger: "#cont4",
        // pin: '#wrapper',   
        start: "-100% 90%", 
        },
        x:0,opacity:1, duration:1
    })
    tl2.fromTo("#price3",{x:-60,opacity:0}, {
        scrollTrigger: {
        trigger: "#cont4",
        // pin: '#wrapper',   
        start: "-100% 90%", 
        },
        x:0,opacity:1, duration:1
    })


    
}


        // nice scroll


function myFunction() {
    var lexilot= document.getElementById('lexilot');
        if ($(window).width() < 900) {
            gsap.to("html",{overflowY:'scroll'})
            window.scrollTo(0, 0);


        }
        if ($(window).width() > 900) {
            gsap.to("html",{overflowY:'scroll'})

            window.scrollTo(0, 0);

            // if (lexilot.style.display=="none"){
            //     $("html").niceScroll({
            //         cursorwidth:4,
            //         autohidemode:false,
            //         cursorcolor:"#F9A0DE",
            //         cursorborder:'none',
            //         scrollspeed: 50,
            //         horizrailenabled:false,
            //         zindex:99999999,
            //     });
            // }
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
}
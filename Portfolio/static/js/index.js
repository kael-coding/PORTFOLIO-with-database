            const sections = document.querySelectorAll('section');
            const navLinks = document.querySelectorAll('.navbar a');

            window.addEventListener('scroll', () => {
                let current = '';

                sections.forEach(section => {
                    const sectionTop = section.offsetTop;
                    const sectionHeight = section.clientHeight;

                    if (pageYOffset >= sectionTop - sectionHeight / 3) {
                        current = section.getAttribute('id');
                    }
                });

                navLinks.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href').includes(current)) {
                        link.classList.add('active');
                    }
                });
            });

            document.getElementById('menu-btn').addEventListener('click', () => {
                const navbar = document.querySelector('.navbar');
                navbar.classList.toggle('active');
            });
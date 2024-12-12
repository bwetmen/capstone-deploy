        // Search bar
        document.getElementById('searchForm').addEventListener('submit', function(event) {
            event.preventDefault();
            var searchQuery = document.getElementById('searchInput').value.toLowerCase();
            var allSections = document.querySelectorAll('section');
            allSections.forEach(function(section) {
                var sectionText = section.textContent.toLowerCase();
                if (sectionText.includes(searchQuery)) {
                    var offset = section.getBoundingClientRect().top;
                    window.scrollBy({ top: offset - 100, left: 0, behavior: 'smooth' });
                    return;
                }
            });
        });

        // Date Button
        document.getElementById("dateButton").addEventListener("click", displayDate);
        function displayDate() {
        document.getElementById("date").innerHTML = Date();
        }

        // JS Onclick Atribute
        var button = document.getElementById("byeButton");
        button.addEventListener("click", function() {
            if (button.textContent === "Klik saya") {
                button.textContent = "Terimakasih Sudah Mengunjungi Website Saya";
            } else {
                button.textContent = "Sampai Jumpa!";
            }
        });

        // Card foto FATISDA
        $(document).ready(function() {
            const fatisda = [
                { src: 'images/lab1_informatika.png', keterangan: 'Lab 1 FATISDA', lokasi: 'Gedung B FMIPA Lantai 4' },
                { src: 'images/lab2_informatika.png', keterangan: 'Lab 2 FATISDA', lokasi: 'Gedung B FMIPA Lantai 4' },
                { src: 'images/room_informatka.png', keterangan: 'Ruang Sidang FATISDA', lokasi: 'Gedung B FMIPA Lantai 4' },
                { src: 'images/office_informatika.png', keterangan: 'Kantor FATISDA', lokasi: 'Gedung B FMIPA Lantai 4' }
            ];

        function loadfatisda() {
            const fatisdaContainer = $('#fatisda-container');
            fatisdaContainer.empty();

            fatisda.forEach(image => {
                const fatisdaCard = createfatisdaCard(image);
                fatisdaContainer.append(fatisdaCard);
            });
        }

        function createfatisdaCard(image) {
            const card = document.createElement('div');
            card.classList.add('card', 'm-2');

            const img = document.createElement('img');
            img.src = image.src;
            img.alt = image.keterangan;
            img.classList.add('card-img-top');

            const cardBody = document.createElement('div');
            cardBody.classList.add('card-body');

            const cardTitle = document.createElement('h5');
            cardTitle.classList.add('card-title');
            cardTitle.textContent = image.keterangan;

            const cardText1 = document.createElement('p');
            cardText1.classList.add('card-text');
            cardText1.textContent = image.lokasi;

            cardBody.appendChild(cardTitle);
            cardBody.appendChild(cardText1);
            card.appendChild(img);
            card.appendChild(cardBody);

            return card;
        }

        // Add foto Fatisda
        function addPhoto(event) {
            event.preventDefault();

            const imageInput = $('#image-input');
            const lokasiInput = $('#lokasi-input');
            const keteranganInput = $('#keterangan-input');

            const newImage = {
                src: imageInput.val(),
                keterangan: keteranganInput.val(),
                lokasi: lokasiInput.val()
            };

            fatisda.push(newImage);
            const fatisdaCard = createfatisdaCard(newImage);
            $('#fatisda-container').append(fatisdaCard);

            imageInput.val('');
            lokasiInput.val('');
            keteranganInput.val('');
        }

        $('#add-foto-uns').on('submit', addPhoto);

        loadfatisda();
        });

        // Scanning 
        const uploadForm = document.getElementById("upload-form");
        const loadingIndicator = document.getElementById("loading-indicator");
        const resultSection = document.getElementById("result");

        uploadForm.addEventListener("submit", function (e) {
            e.preventDefault();

            loadingIndicator.style.display = "block";
            resultSection.style.display = "none";

            setTimeout(() => {
                loadingIndicator.style.display = "none";
                resultSection.style.display = "block";
                document.getElementById("result-text").innerText = "Your analysis result will be shown here!";
            }, 3000); 
        });

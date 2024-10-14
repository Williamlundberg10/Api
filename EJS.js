(function(global) {
    const EJS = {
        // Hämta element från DOM med selektor
        get: function(selector) {
            return document.querySelector(selector);
        },

        // Hämta ett element med ett specifikt id
        get_Id: function(id) {
            const element = document.getElementById(id);
            return element; // Return null if the element does not exist
        },

        // Hämta flera element från DOM
        getAll: function(selector) {
            return document.querySelectorAll(selector);
        },

        // Lägg till en händelsehanterare
        on: function(selector, event, tag, callback) {
            let element; // Declare the variable to hold the element

            // Get element by tag type
            if (tag === 'id') {
                element = this.get_Id(selector); // Get element by ID
            } else {
                element = this.get('.' + selector); // Get element by class selector
            }

            if (element) {
                element.addEventListener(event, callback); // Add the event listener to the DOM element
            } else {
                console.warn(`Element not found for selector: ${selector}`);
            }
        },

        // Gör ett enkelt AJAX-anrop
        ajax: function(url, method = 'GET', data = null, callback) {
            const xhr = new XMLHttpRequest();
            xhr.open(method, url, true);
            xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
            
            xhr.onload = function() {
                if (xhr.status >= 200 && xhr.status < 300) {
                    try {
                        const response = JSON.parse(xhr.responseText);
                        callback(null, response);
                    } catch (e) {
                        callback('Error parsing response');
                    }
                } else {
                    callback(xhr.statusText);
                }
            };

            xhr.onerror = function() {
                callback('Network error');
            };

            xhr.send(data ? JSON.stringify(data) : null);
        },

        // Iterera över en lista av element med en callback-funktion
        forEach: function(elements, callback) {
            elements.forEach(callback);
        },

        // Generell for-loop
        forLoop: function(start, end, callback) {
            for (let i = start; i <= end; i++) {
                callback(i);
            }
        },
    };

    // Exponera biblioteket till globala objektet
    global.EJS = EJS;

})(window);

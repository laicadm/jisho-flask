document.addEventListener('DOMContentLoaded', function() {
    // clear search
    document.getElementById('clear-button').addEventListener('click', function() {
        document.getElementById('keyword-input').value = '';
    });

    document.getElementById('search-form').removeEventListener('submit', formSubmitHandler);
    document.getElementById('search-form').addEventListener('submit', formSubmitHandler);

    document.getElementById('dynamic-search-1').addEventListener('click', dynamicSearch);
    document.getElementById('dynamic-search-2').addEventListener('click', dynamicSearch);
    document.getElementById('dynamic-search-3').addEventListener('click', dynamicSearch);
    document.getElementById('dynamic-search-4').addEventListener('click', dynamicSearch);
    document.getElementById('dynamic-search-5').addEventListener('click', dynamicSearch);

    function dynamicSearch(event) {
        event.preventDefault();
        var keyword = this.getAttribute('data-keyword');
        var form = document.createElement('form');
        form.method = 'POST';
        form.action = this.getAttribute('data-url');
        
        var hiddenField = document.createElement('input');
        hiddenField.type = 'hidden';
        hiddenField.name = 'keyword';
        hiddenField.value = keyword;
        form.appendChild(hiddenField);

        document.body.appendChild(form);
        form.submit();
    }

    function formSubmitHandler(event) {
        event.preventDefault();
    
        var keywordInput = document.getElementById('keyword-input').value;
        if (keywordInput != "") {
            var formAction = this.action;
            var newAction = formAction + '?keyword=' + encodeURIComponent(keywordInput);
        
            this.action = newAction;
            this.submit();
        }
    }

});

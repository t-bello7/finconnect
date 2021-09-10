const categoryField = document.querySelector('#categoryField');
const stateField = document.querySelector('#stateField');
const searchField = document.querySelector('#searchField');


searchField.addEventListener('keyup', (e)=>
{
    const searchValue = e.target.value
    if(searchValue.trim().length>0){
        // console.log(searchValue)
        fetch('/search-listings',{
            body :JSON.stringify({ searchText:searchValue}),
            method: "POST"
        }).then((res) => res.json())
        .then((data) =>{
            console.log('data',data);
            if (data.length === 0){
                console.log('No results found');
            } else {
                location.href = '/search-listings'
                data.forEach((item) =>{

                })
            }
        })
    }
})

// document.querySelectorAll('#searchForm').forEach(item => {
//     item.addEventListener('click', event => {
//       //handle click
//     })
//   })
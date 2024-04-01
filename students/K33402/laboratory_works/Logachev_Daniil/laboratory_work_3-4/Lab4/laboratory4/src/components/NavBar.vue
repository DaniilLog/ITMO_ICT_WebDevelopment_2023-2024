<template>
    <nav>
        <h1>Navigation</h1>
        <ul>
            <li>
            <ul label="Books">
                <li><router-link to="/books">All Books</router-link></li>
                <li><router-link to="/books/new">Add new book</router-link></li>
                <li><router-link to="/books/random">Get random book</router-link></li>
            </ul>
            </li>

            <li>
            <ul label="Readers">
                <li><router-link to="/readers">All Readers</router-link></li>
                <li><router-link to="/readers/new">Add new reader</router-link></li>
            </ul>
            </li>

            <li>
            <ul label="Assignments">
                <li><router-link to="/assignments">All Assignments</router-link></li>
                <li><router-link to="/assignments/new">Add new assignment</router-link></li>
            </ul>
            </li>

            <li>
            <ul label="Halls">
                <li><router-link to="/halls">All Halls</router-link></li>
                <li><router-link to="/halls/new">Add new hall</router-link></li>
            </ul>
            </li>

            <li>
            <ul label="Copies">
                <li><router-link to="/copies">All Copies</router-link></li>
                <li><router-link to="/copies/new">Add new copy</router-link></li>
            </ul>
            </li>
        </ul>
        <h2><router-link to="/logout">Log out</router-link></h2>
    </nav>
</template>

<style scoped>
    ul:before {
        content: attr(label);
        font-size: 120%;
        font-weight: bold;
        color: #000;
    }

    h1 {
        color: #000;
        padding-left: 20px;
    }

    nav {
        padding-right: 50px;
        background-color: #f0f0f0;
        line-height: 200%;
        margin-right: 75px;
        width: 250px;
        height: 100%;
        position: fixed;
        top: 0;
        left: 0;
        
    }

    ul {
        padding-inline-start: 10px;
    }
</style>
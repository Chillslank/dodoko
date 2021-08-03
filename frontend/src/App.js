import { Header } from "./components/header";
import { Login } from "./components/login";
import { Main } from "./components/main"
import { Signup } from "./components/signup";
import { Categories } from "./components/categories"
import { Category } from "./components/category"
// import { Game } from "./components/game"
import { Wishlist } from "./components/wishlist"
function App() {
  return (
    <div className="App">
      <Header />
      {/* <Main /> */}
      {/* <Login /> */}
      {/* <Signup /> */}
      {/* <Category /> */}
      {/* <Categories /> */}
      {/* <Game /> */}
      <Wishlist />
    </div>
  );
}

export default App;

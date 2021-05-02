const app = require("express")();
const server = require("http").createServer(app);
const cors = require("cors");

app.use(cors());

const io = require("socket.io")(server, {
	cors: {
		origin: "*",
		methods: [ "GET", "POST" ]
	}
});

app.get('/', (req, res) => {
	res.send('Server is running');
});

io.on("connection", (socket) => {
	socket.emit("me", socket.id);

	socket.on("disconnect", () => {
		socket.broadcast.emit("callEnded")
	});

	socket.on("callUser", ({ userToCall, signalData, from, name }) => {
		io.to(userToCall).emit("callUser", { signal: signalData, from, name });
	});

	socket.on("answerCall", (data) => {
		io.to(data.to).emit("callAccepted", data.signal)
	});
});

const PORT =  5000;
server.listen(PORT, () => console.log(`Server is running on port ${PORT}`));

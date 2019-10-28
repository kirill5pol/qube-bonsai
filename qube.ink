inkling "2.0"

using Number
experiment {
    num_workers: "3",
    env_runners_per_sampler: "2"
}

type GameState {
    theta: number,
    alpha: number,
    theta_dot: number,
    alpha_dot: number
}

type Action {
    command: Number.Float32<-3..3> # Max voltage -3V to 3V
}

type QubeConfig {
    episode_length: 2048,
    deque_size: 1
}

simulator QubeSimulator(action: Action, config: QubeConfig): GameState {
}

graph (input: GameState): Action {
    concept HighScore(input): Action {
        experiment {
            random_seed: "42"
        }
        curriculum {
            source QubeSimulator
        }
    }
    output HighScore
}
